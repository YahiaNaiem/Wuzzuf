import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:html/parser.dart' as parser;

Future<void> scrapeJobsData(List<String> jobsList) async {
  try {
    var file = File('jobs_data.json');
    var exists = await file.exists();
    var allJobsData = exists ? json.decode(await file.readAsString()) : {};

    for (var jobSearch in jobsList) {
      var response = await http.get(Uri.parse(
          'https://wuzzuf.net/search/jobs/?a=hpb&q=$jobSearch&start=0'));
      var document = parser.parse(response.body);
      var numJobsText =
          document.querySelector('strong')!.text.replaceAll(',', '');
      var numJobs = int.parse(numJobsText);
      var jobsCounter = 1;
      var pageNumber = 0;
      var skillsCount = {};

      while (jobsCounter <= numJobs) {
        response = await http.get(Uri.parse(
            'https://wuzzuf.net/search/jobs/?a=hpb&q=$jobSearch&start=$pageNumber'));
        document = parser.parse(response.body);
        var pageJobs = document.querySelectorAll('.css-1gatmva.e1v1l3u10');

        for (var job in pageJobs) {
          jobsCounter++;
          var skillsTags = job
              .querySelector('.css-y4udm8')!
              .querySelectorAll('div')[1]
              .querySelectorAll('a')
              .sublist(0, 4);
          var skillsText =
              skillsTags.map((e) => e.text.trim().replaceFirst(' · ', ''));
          skillsText.forEach((skill) {
            skillsCount[skill.toLowerCase()] =
                (skillsCount[skill.toLowerCase()] ?? 0) + 1;
          });
        }

        pageNumber++;
        print('${jobsCounter - 1} jobs were scraped');
        print('$pageNumber pages were scraped');
      }

      var sortedSkills = Map.fromEntries(
          skillsCount.entries.toList()..sort((a, b) => b.value.compareTo(a.value)));
      var reducedDict = Map.fromEntries(sortedSkills.entries
          .where((entry) => entry.value > 4));
      allJobsData[jobSearch.replaceAll(' ', '-')] = reducedDict;
    }

    await file.writeAsString(json.encode(allJobsData));
  } catch (e) {
    print('Error: $e');
  }
}

void main() {
  var jobsList = [
    'data scientist',
    'data analyst',
    'web developer',
    'web designer',
    'HR',
    'business developer',
    'mobile development',
    'flutter developer'
  ];

  scrapeJobsData(jobsList);
}
