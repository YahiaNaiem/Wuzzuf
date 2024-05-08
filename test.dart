import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:html/parser.dart' show parse;

// Function to scrape job data from a single page
Future<Map<String, int>> scrapeJobsFromPage(String jobSearch, int pageNumber) async {
  final url = Uri.parse('https://wuzzuf.net/search/jobs/?a=hpb&q=$jobSearch&start=$pageNumber');
  final response = await http.get(url);

  if (response.statusCode == 200) {
    final document = parse(response.body);
    final numJobsText = document.querySelector('strong')?.text;
    if (numJobsText != null) {
      final numJobs = int.parse(numJobsText.replaceAll(',', ''));

      final jobListings = document.querySelectorAll('div.css-1gatmva.e1v1l3u10');
      final skillsCount = {};

      for (final jobListing in jobListings) {
        final skillsSection = jobListing.querySelector('div.css-y4udm8')?.children?.first?.children?.where((e) => e.tagName == 'a');
        if (skillsSection != null) {
          final skills = skillsSection.take(4).map((skill) => skill.text.trimLeft()).toList();
          for (final skill in skills) {
            skillsCount[skill.toLowerCase()] = (skillsCount[skill.toLowerCase()] ?? 0) + 1;
          }
        }
      }

      return skillsCount;
    } else {
      throw Exception('Could not find number of jobs on page $pageNumber');
    }
  } else {
    throw Exception('Failed to fetch page $pageNumber. Status code: ${response.statusCode}');
  }
}

// Function to scrape job data across all pages for a search
Future<Map<String, Map<String, int>>> scrapeAllJobsData(List<String> jobsList) async {
  final allJobsData = {};

  for (final jobSearch in jobsList) {
    final skillsMap = {};
    var pageNumber = 0;
    var totalJobs = 0;

    // Scrape data from first page to get total number of jobs
    try {
      final firstPageSkills = await scrapeJobsFromPage(jobSearch, pageNumber);
      skillsMap.addAll(firstPageSkills);
      totalJobs = (firstPageSkills['total jobs'] ?? 0); // Hypothetical case where total jobs might be found in the first page
    } catch (e) {
      // Handle first page scraping error
      print('Error scraping first page for $jobSearch: $e');
    }

    // Scrape remaining pages until all jobs are retrieved
    while (skillsMap.length < totalJobs) {
      pageNumber++;
      try {
        final pageSkills = await scrapeJobsFromPage(jobSearch, pageNumber);
        skillsMap.addAll(pageSkills);
      } catch (e) {
        // Handle error scraping subsequent pages
        print('Error scraping page $pageNumber for $jobSearch: $e');
      }
    }

    allJobsData[jobSearch.replaceAll(' ', '-')] = Map.from(skillsMap)
      ..removeWhere((key, value) => value <= 4); // Filter out skills with count <= 4
  }

  return allJobsData;
}

void main() async {
  final jobsList = [
    'data scientist',
    'data analyst',
    'web developer',
    'web designer',
    'HR',
    'business developer',
    'mobile development',
    'flutter developer',
  ];

  // Load existing data, if any (replace with your implementation)
  final existingData = {}; // <-- Implement logic to load existing data

  final jobsToScrape = jobsList.where((job) => !existingData.containsKey(job.replaceAll(' ', '-'))).toList();

  try {
    final allJobsData = await scrapeAllJobsData(jobsToScrape);
    // Save data (replace with your implementation)
    // ...
    print('Job data scraped successfully!');
  } catch (e) {
    print('Error scraping job data: $e');
  }
}
