{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "view-in-github"
   },
   "source": [
    "<a href=\"https://colab.research.google.com/github/YahiaNaiem/Wuzzuf/blob/main/Wuzzuf_scrabing.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "3wRIJyj0g7iI",
    "outputId": "0356738a-2928-4d6c-fee9-831a327c4e1f",
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15 jobs were scraped\n",
      "1 pages were scraped\n",
      "30 jobs were scraped\n",
      "2 pages were scraped\n",
      "45 jobs were scraped\n",
      "3 pages were scraped\n",
      "60 jobs were scraped\n",
      "4 pages were scraped\n",
      "75 jobs were scraped\n",
      "5 pages were scraped\n",
      "84 jobs were scraped\n",
      "6 pages were scraped\n",
      "15 jobs were scraped\n",
      "1 pages were scraped\n",
      "30 jobs were scraped\n",
      "2 pages were scraped\n",
      "45 jobs were scraped\n",
      "3 pages were scraped\n",
      "60 jobs were scraped\n",
      "4 pages were scraped\n",
      "75 jobs were scraped\n",
      "5 pages were scraped\n",
      "90 jobs were scraped\n",
      "6 pages were scraped\n",
      "105 jobs were scraped\n",
      "7 pages were scraped\n",
      "120 jobs were scraped\n",
      "8 pages were scraped\n",
      "135 jobs were scraped\n",
      "9 pages were scraped\n",
      "150 jobs were scraped\n",
      "10 pages were scraped\n",
      "165 jobs were scraped\n",
      "11 pages were scraped\n",
      "180 jobs were scraped\n",
      "12 pages were scraped\n",
      "195 jobs were scraped\n",
      "13 pages were scraped\n",
      "210 jobs were scraped\n",
      "14 pages were scraped\n",
      "225 jobs were scraped\n",
      "15 pages were scraped\n",
      "240 jobs were scraped\n",
      "16 pages were scraped\n",
      "255 jobs were scraped\n",
      "17 pages were scraped\n",
      "270 jobs were scraped\n",
      "18 pages were scraped\n",
      "285 jobs were scraped\n",
      "19 pages were scraped\n",
      "300 jobs were scraped\n",
      "20 pages were scraped\n",
      "315 jobs were scraped\n",
      "21 pages were scraped\n",
      "330 jobs were scraped\n",
      "22 pages were scraped\n",
      "345 jobs were scraped\n",
      "23 pages were scraped\n",
      "360 jobs were scraped\n",
      "24 pages were scraped\n",
      "375 jobs were scraped\n",
      "25 pages were scraped\n",
      "390 jobs were scraped\n",
      "26 pages were scraped\n",
      "405 jobs were scraped\n",
      "27 pages were scraped\n",
      "420 jobs were scraped\n",
      "28 pages were scraped\n",
      "435 jobs were scraped\n",
      "29 pages were scraped\n",
      "450 jobs were scraped\n",
      "30 pages were scraped\n",
      "465 jobs were scraped\n",
      "31 pages were scraped\n",
      "480 jobs were scraped\n",
      "32 pages were scraped\n",
      "495 jobs were scraped\n",
      "33 pages were scraped\n",
      "510 jobs were scraped\n",
      "34 pages were scraped\n",
      "525 jobs were scraped\n",
      "35 pages were scraped\n",
      "540 jobs were scraped\n",
      "36 pages were scraped\n",
      "555 jobs were scraped\n",
      "37 pages were scraped\n",
      "570 jobs were scraped\n",
      "38 pages were scraped\n",
      "585 jobs were scraped\n",
      "39 pages were scraped\n",
      "600 jobs were scraped\n",
      "40 pages were scraped\n",
      "615 jobs were scraped\n",
      "41 pages were scraped\n",
      "630 jobs were scraped\n",
      "42 pages were scraped\n",
      "645 jobs were scraped\n",
      "43 pages were scraped\n",
      "660 jobs were scraped\n",
      "44 pages were scraped\n",
      "675 jobs were scraped\n",
      "45 pages were scraped\n",
      "690 jobs were scraped\n",
      "46 pages were scraped\n",
      "705 jobs were scraped\n",
      "47 pages were scraped\n",
      "720 jobs were scraped\n",
      "48 pages were scraped\n",
      "735 jobs were scraped\n",
      "49 pages were scraped\n",
      "750 jobs were scraped\n",
      "50 pages were scraped\n",
      "765 jobs were scraped\n",
      "51 pages were scraped\n",
      "780 jobs were scraped\n",
      "52 pages were scraped\n",
      "795 jobs were scraped\n",
      "53 pages were scraped\n",
      "810 jobs were scraped\n",
      "54 pages were scraped\n",
      "825 jobs were scraped\n",
      "55 pages were scraped\n",
      "840 jobs were scraped\n",
      "56 pages were scraped\n",
      "855 jobs were scraped\n",
      "57 pages were scraped\n",
      "870 jobs were scraped\n",
      "58 pages were scraped\n",
      "885 jobs were scraped\n",
      "59 pages were scraped\n",
      "900 jobs were scraped\n",
      "60 pages were scraped\n",
      "915 jobs were scraped\n",
      "61 pages were scraped\n",
      "930 jobs were scraped\n",
      "62 pages were scraped\n",
      "945 jobs were scraped\n",
      "63 pages were scraped\n",
      "960 jobs were scraped\n",
      "64 pages were scraped\n",
      "975 jobs were scraped\n",
      "65 pages were scraped\n",
      "990 jobs were scraped\n",
      "66 pages were scraped\n",
      "1005 jobs were scraped\n",
      "67 pages were scraped\n",
      "1020 jobs were scraped\n",
      "68 pages were scraped\n",
      "1035 jobs were scraped\n",
      "69 pages were scraped\n",
      "1050 jobs were scraped\n",
      "70 pages were scraped\n",
      "1065 jobs were scraped\n",
      "71 pages were scraped\n",
      "1080 jobs were scraped\n",
      "72 pages were scraped\n",
      "1095 jobs were scraped\n",
      "73 pages were scraped\n",
      "1110 jobs were scraped\n",
      "74 pages were scraped\n",
      "1125 jobs were scraped\n",
      "75 pages were scraped\n",
      "1140 jobs were scraped\n",
      "76 pages were scraped\n",
      "1155 jobs were scraped\n",
      "77 pages were scraped\n",
      "1170 jobs were scraped\n",
      "78 pages were scraped\n",
      "1185 jobs were scraped\n",
      "79 pages were scraped\n",
      "1200 jobs were scraped\n",
      "80 pages were scraped\n",
      "1215 jobs were scraped\n",
      "81 pages were scraped\n",
      "1230 jobs were scraped\n",
      "82 pages were scraped\n",
      "1245 jobs were scraped\n",
      "83 pages were scraped\n",
      "1260 jobs were scraped\n",
      "84 pages were scraped\n",
      "1275 jobs were scraped\n",
      "85 pages were scraped\n",
      "1290 jobs were scraped\n",
      "86 pages were scraped\n",
      "1305 jobs were scraped\n",
      "87 pages were scraped\n",
      "1320 jobs were scraped\n",
      "88 pages were scraped\n",
      "1335 jobs were scraped\n",
      "89 pages were scraped\n",
      "1350 jobs were scraped\n",
      "90 pages were scraped\n",
      "1365 jobs were scraped\n",
      "91 pages were scraped\n",
      "1380 jobs were scraped\n",
      "92 pages were scraped\n",
      "1395 jobs were scraped\n",
      "93 pages were scraped\n",
      "1410 jobs were scraped\n",
      "94 pages were scraped\n",
      "1425 jobs were scraped\n",
      "95 pages were scraped\n",
      "1440 jobs were scraped\n",
      "96 pages were scraped\n",
      "1455 jobs were scraped\n",
      "97 pages were scraped\n",
      "1470 jobs were scraped\n",
      "98 pages were scraped\n",
      "1485 jobs were scraped\n",
      "99 pages were scraped\n",
      "1500 jobs were scraped\n",
      "100 pages were scraped\n",
      "1515 jobs were scraped\n",
      "101 pages were scraped\n",
      "1530 jobs were scraped\n",
      "102 pages were scraped\n",
      "1545 jobs were scraped\n",
      "103 pages were scraped\n",
      "1560 jobs were scraped\n",
      "104 pages were scraped\n",
      "1575 jobs were scraped\n",
      "105 pages were scraped\n",
      "1590 jobs were scraped\n",
      "106 pages were scraped\n",
      "1605 jobs were scraped\n",
      "107 pages were scraped\n",
      "1620 jobs were scraped\n",
      "108 pages were scraped\n",
      "1635 jobs were scraped\n",
      "109 pages were scraped\n",
      "1650 jobs were scraped\n",
      "110 pages were scraped\n",
      "1665 jobs were scraped\n",
      "111 pages were scraped\n",
      "1680 jobs were scraped\n",
      "112 pages were scraped\n",
      "1695 jobs were scraped\n",
      "113 pages were scraped\n",
      "1710 jobs were scraped\n",
      "114 pages were scraped\n",
      "1725 jobs were scraped\n",
      "115 pages were scraped\n",
      "1740 jobs were scraped\n",
      "116 pages were scraped\n",
      "1755 jobs were scraped\n",
      "117 pages were scraped\n",
      "1770 jobs were scraped\n",
      "118 pages were scraped\n",
      "1785 jobs were scraped\n",
      "119 pages were scraped\n",
      "1800 jobs were scraped\n",
      "120 pages were scraped\n",
      "1815 jobs were scraped\n",
      "121 pages were scraped\n",
      "1830 jobs were scraped\n",
      "122 pages were scraped\n",
      "1845 jobs were scraped\n",
      "123 pages were scraped\n",
      "1860 jobs were scraped\n",
      "124 pages were scraped\n",
      "1875 jobs were scraped\n",
      "125 pages were scraped\n",
      "1890 jobs were scraped\n",
      "126 pages were scraped\n",
      "1905 jobs were scraped\n",
      "127 pages were scraped\n",
      "1920 jobs were scraped\n",
      "128 pages were scraped\n",
      "1935 jobs were scraped\n",
      "129 pages were scraped\n",
      "1950 jobs were scraped\n",
      "130 pages were scraped\n",
      "1965 jobs were scraped\n",
      "131 pages were scraped\n",
      "1980 jobs were scraped\n",
      "132 pages were scraped\n",
      "1995 jobs were scraped\n",
      "133 pages were scraped\n",
      "2010 jobs were scraped\n",
      "134 pages were scraped\n",
      "2025 jobs were scraped\n",
      "135 pages were scraped\n",
      "2040 jobs were scraped\n",
      "136 pages were scraped\n",
      "2055 jobs were scraped\n",
      "137 pages were scraped\n",
      "2070 jobs were scraped\n",
      "138 pages were scraped\n",
      "2085 jobs were scraped\n",
      "139 pages were scraped\n",
      "2100 jobs were scraped\n",
      "140 pages were scraped\n",
      "2115 jobs were scraped\n",
      "141 pages were scraped\n",
      "2130 jobs were scraped\n",
      "142 pages were scraped\n",
      "2145 jobs were scraped\n",
      "143 pages were scraped\n",
      "2160 jobs were scraped\n",
      "144 pages were scraped\n",
      "2175 jobs were scraped\n",
      "145 pages were scraped\n",
      "2190 jobs were scraped\n",
      "146 pages were scraped\n",
      "2205 jobs were scraped\n",
      "147 pages were scraped\n",
      "2220 jobs were scraped\n",
      "148 pages were scraped\n",
      "2235 jobs were scraped\n",
      "149 pages were scraped\n",
      "2250 jobs were scraped\n",
      "150 pages were scraped\n",
      "2265 jobs were scraped\n",
      "151 pages were scraped\n",
      "2280 jobs were scraped\n",
      "152 pages were scraped\n",
      "2295 jobs were scraped\n",
      "153 pages were scraped\n",
      "2310 jobs were scraped\n",
      "154 pages were scraped\n",
      "2325 jobs were scraped\n",
      "155 pages were scraped\n",
      "2340 jobs were scraped\n",
      "156 pages were scraped\n",
      "2355 jobs were scraped\n",
      "157 pages were scraped\n",
      "2370 jobs were scraped\n",
      "158 pages were scraped\n",
      "2385 jobs were scraped\n",
      "159 pages were scraped\n",
      "2400 jobs were scraped\n",
      "160 pages were scraped\n",
      "2415 jobs were scraped\n",
      "161 pages were scraped\n",
      "2430 jobs were scraped\n",
      "162 pages were scraped\n",
      "2445 jobs were scraped\n",
      "163 pages were scraped\n",
      "2460 jobs were scraped\n",
      "164 pages were scraped\n",
      "2475 jobs were scraped\n",
      "165 pages were scraped\n",
      "2490 jobs were scraped\n",
      "166 pages were scraped\n",
      "2505 jobs were scraped\n",
      "167 pages were scraped\n",
      "2520 jobs were scraped\n",
      "168 pages were scraped\n",
      "2535 jobs were scraped\n",
      "169 pages were scraped\n",
      "2550 jobs were scraped\n",
      "170 pages were scraped\n",
      "2565 jobs were scraped\n",
      "171 pages were scraped\n",
      "2580 jobs were scraped\n",
      "172 pages were scraped\n",
      "2595 jobs were scraped\n",
      "173 pages were scraped\n",
      "2610 jobs were scraped\n",
      "174 pages were scraped\n",
      "2625 jobs were scraped\n",
      "175 pages were scraped\n",
      "2640 jobs were scraped\n",
      "176 pages were scraped\n",
      "2655 jobs were scraped\n",
      "177 pages were scraped\n",
      "2670 jobs were scraped\n",
      "178 pages were scraped\n",
      "2685 jobs were scraped\n",
      "179 pages were scraped\n",
      "2700 jobs were scraped\n",
      "180 pages were scraped\n",
      "2715 jobs were scraped\n",
      "181 pages were scraped\n",
      "2730 jobs were scraped\n",
      "182 pages were scraped\n",
      "2745 jobs were scraped\n",
      "183 pages were scraped\n",
      "2760 jobs were scraped\n",
      "184 pages were scraped\n",
      "2775 jobs were scraped\n",
      "185 pages were scraped\n",
      "2790 jobs were scraped\n",
      "186 pages were scraped\n",
      "2805 jobs were scraped\n",
      "187 pages were scraped\n",
      "2820 jobs were scraped\n",
      "188 pages were scraped\n",
      "2835 jobs were scraped\n",
      "189 pages were scraped\n",
      "2850 jobs were scraped\n",
      "190 pages were scraped\n",
      "2865 jobs were scraped\n",
      "191 pages were scraped\n",
      "2880 jobs were scraped\n",
      "192 pages were scraped\n",
      "2895 jobs were scraped\n",
      "193 pages were scraped\n",
      "2910 jobs were scraped\n",
      "194 pages were scraped\n",
      "2925 jobs were scraped\n",
      "195 pages were scraped\n",
      "2940 jobs were scraped\n",
      "196 pages were scraped\n",
      "2955 jobs were scraped\n",
      "197 pages were scraped\n",
      "2970 jobs were scraped\n",
      "198 pages were scraped\n",
      "2985 jobs were scraped\n",
      "199 pages were scraped\n",
      "3000 jobs were scraped\n",
      "200 pages were scraped\n",
      "3015 jobs were scraped\n",
      "201 pages were scraped\n",
      "3030 jobs were scraped\n",
      "202 pages were scraped\n",
      "3045 jobs were scraped\n",
      "203 pages were scraped\n",
      "3060 jobs were scraped\n",
      "204 pages were scraped\n",
      "3075 jobs were scraped\n",
      "205 pages were scraped\n",
      "3090 jobs were scraped\n",
      "206 pages were scraped\n",
      "3105 jobs were scraped\n",
      "207 pages were scraped\n",
      "3120 jobs were scraped\n",
      "208 pages were scraped\n",
      "3135 jobs were scraped\n",
      "209 pages were scraped\n",
      "3136 jobs were scraped\n",
      "210 pages were scraped\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def insert_skills(jobs_list):\n",
    "    all_jobs_data = {}\n",
    "    for job_search in jobs_list:\n",
    "        response = requests.get(f\"https://wuzzuf.net/search/jobs/?a=hpb&q={job_search}&start=0\")\n",
    "        soup = BeautifulSoup(response.text , \"html.parser\")  #to use in defining the needed values(Num_of_Jobs)\n",
    "        #getting the number of jobs to loop on\n",
    "        num_of_jobs_text = soup.find(\"strong\").get_text()\n",
    "        Num_of_Jobs = int(num_of_jobs_text.replace(',', ''))\n",
    "        jops_counter = 1\n",
    "        page_number = 0\n",
    "        skills_count = {}\n",
    "        while jops_counter <= Num_of_Jobs: #loop for the number of jobs in all pages\n",
    "            response = requests.get(f\"https://wuzzuf.net/search/jobs/?a=hpb&q={job_search}&start={page_number}\")\n",
    "            soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "            page_jobs = soup.find_all(\"div\", attrs={\"class\": \"css-1gatmva e1v1l3u10\"})\n",
    "        \n",
    "            for job in page_jobs: #loop for jobs in each page\n",
    "                jops_counter += 1\n",
    "                skills_tags = job.find(\"div\", attrs={\"class\": \"css-y4udm8\"}).find_all(\"div\", attrs={})[1].find_all(\"a\", attrs={\"class\": \"css-5x9pm1\"})[0:4]\n",
    "                try:\n",
    "                    skills_text = [skill.get_text().lstrip(' · ') for skill in skills_tags]\n",
    "                except:\n",
    "                    continue\n",
    "        \n",
    "                # Update skills_count dictionary\n",
    "                for skill in skills_text:\n",
    "                    skills_count[skill.lower()] = skills_count.get(skill.lower(), 0) + 1\n",
    "        \n",
    "            page_number += 1\n",
    "            print(f\"{jops_counter - 1} jobs were scraped\")\n",
    "            print(f\"{page_number} pages were scraped\")\n",
    "        \n",
    "        sorted_skills = dict(sorted(skills_count.items(), key = lambda item: item[1], reverse = True))\n",
    "        reduced_dict = {key: value for key, value in sorted_skills.items() if value > 4}\n",
    "        all_jobs_data[job_search] = reduced_dict\n",
    "        \n",
    "    with open('jobs_data.json', 'w') as json_file:\n",
    "        json.dump(all_jobs_data, json_file, indent=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15 jobs were scraped\n",
      "1 pages were scraped\n",
      "30 jobs were scraped\n",
      "2 pages were scraped\n",
      "45 jobs were scraped\n",
      "3 pages were scraped\n",
      "60 jobs were scraped\n",
      "4 pages were scraped\n",
      "75 jobs were scraped\n",
      "5 pages were scraped\n",
      "90 jobs were scraped\n",
      "6 pages were scraped\n",
      "105 jobs were scraped\n",
      "7 pages were scraped\n",
      "120 jobs were scraped\n",
      "8 pages were scraped\n",
      "135 jobs were scraped\n",
      "9 pages were scraped\n",
      "150 jobs were scraped\n",
      "10 pages were scraped\n",
      "165 jobs were scraped\n",
      "11 pages were scraped\n",
      "180 jobs were scraped\n",
      "12 pages were scraped\n",
      "195 jobs were scraped\n",
      "13 pages were scraped\n",
      "210 jobs were scraped\n",
      "14 pages were scraped\n",
      "225 jobs were scraped\n",
      "15 pages were scraped\n",
      "240 jobs were scraped\n",
      "16 pages were scraped\n",
      "255 jobs were scraped\n",
      "17 pages were scraped\n",
      "270 jobs were scraped\n",
      "18 pages were scraped\n",
      "285 jobs were scraped\n",
      "19 pages were scraped\n",
      "300 jobs were scraped\n",
      "20 pages were scraped\n",
      "315 jobs were scraped\n",
      "21 pages were scraped\n",
      "330 jobs were scraped\n",
      "22 pages were scraped\n",
      "345 jobs were scraped\n",
      "23 pages were scraped\n",
      "360 jobs were scraped\n",
      "24 pages were scraped\n",
      "375 jobs were scraped\n",
      "25 pages were scraped\n",
      "390 jobs were scraped\n",
      "26 pages were scraped\n",
      "405 jobs were scraped\n",
      "27 pages were scraped\n",
      "420 jobs were scraped\n",
      "28 pages were scraped\n",
      "435 jobs were scraped\n",
      "29 pages were scraped\n",
      "450 jobs were scraped\n",
      "30 pages were scraped\n",
      "465 jobs were scraped\n",
      "31 pages were scraped\n",
      "480 jobs were scraped\n",
      "32 pages were scraped\n",
      "495 jobs were scraped\n",
      "33 pages were scraped\n",
      "510 jobs were scraped\n",
      "34 pages were scraped\n",
      "525 jobs were scraped\n",
      "35 pages were scraped\n",
      "540 jobs were scraped\n",
      "36 pages were scraped\n",
      "555 jobs were scraped\n",
      "37 pages were scraped\n",
      "570 jobs were scraped\n",
      "38 pages were scraped\n",
      "585 jobs were scraped\n",
      "39 pages were scraped\n",
      "600 jobs were scraped\n",
      "40 pages were scraped\n",
      "615 jobs were scraped\n",
      "41 pages were scraped\n",
      "630 jobs were scraped\n",
      "42 pages were scraped\n",
      "645 jobs were scraped\n",
      "43 pages were scraped\n",
      "660 jobs were scraped\n",
      "44 pages were scraped\n",
      "675 jobs were scraped\n",
      "45 pages were scraped\n",
      "690 jobs were scraped\n",
      "46 pages were scraped\n",
      "705 jobs were scraped\n",
      "47 pages were scraped\n",
      "720 jobs were scraped\n",
      "48 pages were scraped\n",
      "735 jobs were scraped\n",
      "49 pages were scraped\n",
      "750 jobs were scraped\n",
      "50 pages were scraped\n",
      "765 jobs were scraped\n",
      "51 pages were scraped\n",
      "780 jobs were scraped\n",
      "52 pages were scraped\n",
      "795 jobs were scraped\n",
      "53 pages were scraped\n",
      "810 jobs were scraped\n",
      "54 pages were scraped\n",
      "825 jobs were scraped\n",
      "55 pages were scraped\n",
      "840 jobs were scraped\n",
      "56 pages were scraped\n",
      "855 jobs were scraped\n",
      "57 pages were scraped\n",
      "870 jobs were scraped\n",
      "58 pages were scraped\n",
      "885 jobs were scraped\n",
      "59 pages were scraped\n",
      "900 jobs were scraped\n",
      "60 pages were scraped\n",
      "915 jobs were scraped\n",
      "61 pages were scraped\n",
      "930 jobs were scraped\n",
      "62 pages were scraped\n",
      "945 jobs were scraped\n",
      "63 pages were scraped\n",
      "960 jobs were scraped\n",
      "64 pages were scraped\n",
      "975 jobs were scraped\n",
      "65 pages were scraped\n",
      "990 jobs were scraped\n",
      "66 pages were scraped\n",
      "1005 jobs were scraped\n",
      "67 pages were scraped\n",
      "1020 jobs were scraped\n",
      "68 pages were scraped\n",
      "1035 jobs were scraped\n",
      "69 pages were scraped\n",
      "1050 jobs were scraped\n",
      "70 pages were scraped\n",
      "1065 jobs were scraped\n",
      "71 pages were scraped\n",
      "1080 jobs were scraped\n",
      "72 pages were scraped\n",
      "1095 jobs were scraped\n",
      "73 pages were scraped\n",
      "1110 jobs were scraped\n",
      "74 pages were scraped\n",
      "1125 jobs were scraped\n",
      "75 pages were scraped\n",
      "1140 jobs were scraped\n",
      "76 pages were scraped\n",
      "1155 jobs were scraped\n",
      "77 pages were scraped\n",
      "1170 jobs were scraped\n",
      "78 pages were scraped\n",
      "1185 jobs were scraped\n",
      "79 pages were scraped\n",
      "1200 jobs were scraped\n",
      "80 pages were scraped\n",
      "1215 jobs were scraped\n",
      "81 pages were scraped\n",
      "1230 jobs were scraped\n",
      "82 pages were scraped\n",
      "1245 jobs were scraped\n",
      "83 pages were scraped\n",
      "1260 jobs were scraped\n",
      "84 pages were scraped\n",
      "1270 jobs were scraped\n",
      "85 pages were scraped\n",
      "15 jobs were scraped\n",
      "1 pages were scraped\n",
      "30 jobs were scraped\n",
      "2 pages were scraped\n",
      "45 jobs were scraped\n",
      "3 pages were scraped\n",
      "60 jobs were scraped\n",
      "4 pages were scraped\n",
      "75 jobs were scraped\n",
      "5 pages were scraped\n",
      "90 jobs were scraped\n",
      "6 pages were scraped\n",
      "105 jobs were scraped\n",
      "7 pages were scraped\n",
      "120 jobs were scraped\n",
      "8 pages were scraped\n",
      "135 jobs were scraped\n",
      "9 pages were scraped\n",
      "150 jobs were scraped\n",
      "10 pages were scraped\n",
      "165 jobs were scraped\n",
      "11 pages were scraped\n",
      "180 jobs were scraped\n",
      "12 pages were scraped\n",
      "195 jobs were scraped\n",
      "13 pages were scraped\n",
      "210 jobs were scraped\n",
      "14 pages were scraped\n",
      "225 jobs were scraped\n",
      "15 pages were scraped\n",
      "240 jobs were scraped\n",
      "16 pages were scraped\n",
      "255 jobs were scraped\n",
      "17 pages were scraped\n",
      "270 jobs were scraped\n",
      "18 pages were scraped\n",
      "285 jobs were scraped\n",
      "19 pages were scraped\n",
      "300 jobs were scraped\n",
      "20 pages were scraped\n",
      "315 jobs were scraped\n",
      "21 pages were scraped\n",
      "330 jobs were scraped\n",
      "22 pages were scraped\n",
      "345 jobs were scraped\n",
      "23 pages were scraped\n",
      "360 jobs were scraped\n",
      "24 pages were scraped\n",
      "375 jobs were scraped\n",
      "25 pages were scraped\n",
      "390 jobs were scraped\n",
      "26 pages were scraped\n",
      "405 jobs were scraped\n",
      "27 pages were scraped\n",
      "420 jobs were scraped\n",
      "28 pages were scraped\n",
      "435 jobs were scraped\n",
      "29 pages were scraped\n",
      "450 jobs were scraped\n",
      "30 pages were scraped\n",
      "465 jobs were scraped\n",
      "31 pages were scraped\n",
      "480 jobs were scraped\n",
      "32 pages were scraped\n",
      "495 jobs were scraped\n",
      "33 pages were scraped\n",
      "510 jobs were scraped\n",
      "34 pages were scraped\n",
      "525 jobs were scraped\n",
      "35 pages were scraped\n",
      "540 jobs were scraped\n",
      "36 pages were scraped\n",
      "555 jobs were scraped\n",
      "37 pages were scraped\n",
      "570 jobs were scraped\n",
      "38 pages were scraped\n",
      "585 jobs were scraped\n",
      "39 pages were scraped\n",
      "600 jobs were scraped\n",
      "40 pages were scraped\n",
      "615 jobs were scraped\n",
      "41 pages were scraped\n",
      "630 jobs were scraped\n",
      "42 pages were scraped\n",
      "645 jobs were scraped\n",
      "43 pages were scraped\n",
      "660 jobs were scraped\n",
      "44 pages were scraped\n",
      "675 jobs were scraped\n",
      "45 pages were scraped\n",
      "690 jobs were scraped\n",
      "46 pages were scraped\n",
      "705 jobs were scraped\n",
      "47 pages were scraped\n",
      "720 jobs were scraped\n",
      "48 pages were scraped\n",
      "735 jobs were scraped\n",
      "49 pages were scraped\n",
      "750 jobs were scraped\n",
      "50 pages were scraped\n",
      "765 jobs were scraped\n",
      "51 pages were scraped\n",
      "780 jobs were scraped\n",
      "52 pages were scraped\n",
      "795 jobs were scraped\n",
      "53 pages were scraped\n",
      "810 jobs were scraped\n",
      "54 pages were scraped\n",
      "825 jobs were scraped\n",
      "55 pages were scraped\n",
      "840 jobs were scraped\n",
      "56 pages were scraped\n",
      "855 jobs were scraped\n",
      "57 pages were scraped\n",
      "870 jobs were scraped\n",
      "58 pages were scraped\n",
      "874 jobs were scraped\n",
      "59 pages were scraped\n"
     ]
    }
   ],
   "source": [
    "jobs_list = ['data scientist', 'software engineer']  # List of job searches\n",
    "insert_skills(jobs_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI\n",
    "from typing import Dict\n",
    "import json\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "def scrape_jobs_data(jobs_list):\n",
    "    all_jobs_data = {}\n",
    "    for job_search in jobs_list:\n",
    "        response = requests.get(f\"https://wuzzuf.net/search/jobs/?a=hpb&q={job_search}&start=0\")\n",
    "        soup = BeautifulSoup(response.text , \"html.parser\")  \n",
    "        num_of_jobs_text = soup.find(\"strong\").get_text()\n",
    "        Num_of_Jobs = int(num_of_jobs_text.replace(',', ''))\n",
    "        jops_counter = 1\n",
    "        page_number = 0\n",
    "        skills_count = {}\n",
    "        while jops_counter <= Num_of_Jobs: \n",
    "            response = requests.get(f\"https://wuzzuf.net/search/jobs/?a=hpb&q={job_search}&start={page_number}\")\n",
    "            soup = BeautifulSoup(response.text, \"html.parser\")\n",
    "            page_jobs = soup.find_all(\"div\", attrs={\"class\": \"css-1gatmva e1v1l3u10\"})\n",
    "        \n",
    "            for job in page_jobs: \n",
    "                jops_counter += 1\n",
    "                skills_tags = job.find(\"div\", attrs={\"class\": \"css-y4udm8\"}).find_all(\"div\", attrs={})[1].find_all(\"a\", attrs={\"class\": \"css-5x9pm1\"})[0:4]\n",
    "                try:\n",
    "                    skills_text = [skill.get_text().lstrip(' · ') for skill in skills_tags]\n",
    "                except:\n",
    "                    continue\n",
    "        \n",
    "                for skill in skills_text:\n",
    "                    skills_count[skill.lower()] = skills_count.get(skill.lower(), 0) + 1\n",
    "        \n",
    "            page_number += 1\n",
    "        \n",
    "        sorted_skills = dict(sorted(skills_count.items(), key = lambda item: item[1], reverse = True))\n",
    "        reduced_dict = {key: value for key, value in sorted_skills.items() if value > 4}\n",
    "        all_jobs_data[job_search] = reduced_dict\n",
    "        \n",
    "    return all_jobs_data\n",
    "\n",
    "@app.get(\"/jobs_data/\")\n",
    "def get_jobs_data():\n",
    "    # Load data from JSON file or scrape if file not found\n",
    "    try:\n",
    "        with open('jobs_data.json', 'r') as json_file:\n",
    "            jobs_data = json.load(json_file)\n",
    "    except FileNotFoundError:\n",
    "        jobs_data = scrape_jobs_data(['data scientist', 'software engineer'])  # Example job searches\n",
    "        with open('jobs_data.json', 'w') as json_file:\n",
    "            json.dump(jobs_data, json_file, indent=4)\n",
    "    \n",
    "    return jobs_data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'data scientist': {'computer science': 46,\n",
       "  'information technology (it)': 45,\n",
       "  'python': 19,\n",
       "  'sql': 16,\n",
       "  'engineering': 15,\n",
       "  'software development': 9,\n",
       "  'sales': 6,\n",
       "  'javascript': 6,\n",
       "  'analysis': 5,\n",
       "  'machine learning': 5,\n",
       "  'accounting': 5,\n",
       "  'finance': 5,\n",
       "  'financial analysis': 5,\n",
       "  'marketing': 5,\n",
       "  'project management': 5,\n",
       "  'customer service': 5,\n",
       "  'sales skills': 5},\n",
       " 'software engineer': {'information technology (it)': 1604,\n",
       "  'computer science': 1434,\n",
       "  'engineering': 1042,\n",
       "  'sales': 373,\n",
       "  'software development': 350,\n",
       "  'project management': 251,\n",
       "  'sales skills': 246,\n",
       "  'customer service': 177,\n",
       "  'autocad': 173,\n",
       "  'microsoft office': 167,\n",
       "  'design': 162,\n",
       "  'software engineering': 158,\n",
       "  'computer engineering': 134,\n",
       "  'mechanical engineering': 130,\n",
       "  'management': 130,\n",
       "  'sales target': 119,\n",
       "  'architecture': 116,\n",
       "  'civil engineering': 108,\n",
       "  'analysis': 95,\n",
       "  'marketing': 86,\n",
       "  'quality control': 84,\n",
       "  'maintenance': 83,\n",
       "  'quality assurance': 81,\n",
       "  'javascript': 81,\n",
       "  'accounting': 80,\n",
       "  'electrical engineering': 79,\n",
       "  'administration': 74,\n",
       "  'agile': 72,\n",
       "  'communication': 71,\n",
       "  'construction': 71,\n",
       "  'business analysis': 70,\n",
       "  'sql': 69,\n",
       "  'customer support': 68,\n",
       "  'technical support': 68,\n",
       "  'pmp': 61,\n",
       "  'customer care': 59,\n",
       "  'communication skills': 56,\n",
       "  'quality': 56,\n",
       "  'finance': 56,\n",
       "  'business development': 53,\n",
       "  'erp': 48,\n",
       "  'python': 46,\n",
       "  'software': 45,\n",
       "  'computer': 44,\n",
       "  'qa': 41,\n",
       "  '.net': 41,\n",
       "  'ccna': 41,\n",
       "  'php': 39,\n",
       "  'revit': 39,\n",
       "  'java': 37,\n",
       "  'development': 36,\n",
       "  'installation': 36,\n",
       "  'angular': 34,\n",
       "  'oracle': 34,\n",
       "  'logistics': 34,\n",
       "  'it': 33,\n",
       "  'english': 32,\n",
       "  'software testing': 32,\n",
       "  'cad': 32,\n",
       "  'civil': 31,\n",
       "  'supply chain': 27,\n",
       "  'education': 27,\n",
       "  'product management': 26,\n",
       "  'business': 25,\n",
       "  'networking': 24,\n",
       "  'sap': 24,\n",
       "  'adobe photoshop': 24,\n",
       "  'android': 23,\n",
       "  'ui': 23,\n",
       "  'data analysis': 23,\n",
       "  'planning': 22,\n",
       "  'human resources (hr)': 22,\n",
       "  'apis': 21,\n",
       "  'html': 21,\n",
       "  'laravel': 21,\n",
       "  'css': 21,\n",
       "  'mechanical': 20,\n",
       "  'database': 20,\n",
       "  'electrical': 20,\n",
       "  'manufacturing': 20,\n",
       "  'operations': 20,\n",
       "  'security': 20,\n",
       "  'automation': 19,\n",
       "  'aws': 19,\n",
       "  'developer': 19,\n",
       "  'ux': 19,\n",
       "  'odoo': 19,\n",
       "  'procurement': 19,\n",
       "  'purchasing': 19,\n",
       "  'financial analysis': 19,\n",
       "  'adobe illustrator': 19,\n",
       "  'devops': 18,\n",
       "  'crm': 18,\n",
       "  'telecommunication': 18,\n",
       "  'programming': 17,\n",
       "  'asp.net': 17,\n",
       "  'testing': 17,\n",
       "  'technical office': 17,\n",
       "  'real estate': 17,\n",
       "  'recruitment': 17,\n",
       "  'html5': 16,\n",
       "  'hvac': 16,\n",
       "  'front-end': 16,\n",
       "  'help desk': 16,\n",
       "  'web development': 15,\n",
       "  'c#': 15,\n",
       "  'qc': 15,\n",
       "  '3d': 15,\n",
       "  'bim': 15,\n",
       "  'cloud': 14,\n",
       "  'backend': 14,\n",
       "  'react': 14,\n",
       "  'teaching': 14,\n",
       "  'business administration': 14,\n",
       "  'graphic design': 14,\n",
       "  'admin': 14,\n",
       "  'api': 13,\n",
       "  'science': 13,\n",
       "  'flutter': 13,\n",
       "  'git': 13,\n",
       "  'production': 13,\n",
       "  'interior design': 13,\n",
       "  'mysql': 13,\n",
       "  'engineer': 12,\n",
       "  'architectural': 12,\n",
       "  'ccnp': 12,\n",
       "  'system administration': 12,\n",
       "  'computer skills': 12,\n",
       "  'project coordination': 12,\n",
       "  'financial management': 12,\n",
       "  'social media': 12,\n",
       "  'project': 11,\n",
       "  'architectural engineering': 11,\n",
       "  'cisco': 11,\n",
       "  'technical': 11,\n",
       "  'information technology': 11,\n",
       "  'css3': 10,\n",
       "  'mobile development': 10,\n",
       "  'ios': 10,\n",
       "  'full stack': 10,\n",
       "  'node.js': 10,\n",
       "  'linux': 10,\n",
       "  'infrastructure': 10,\n",
       "  'architect': 10,\n",
       "  'call center': 10,\n",
       "  'information systems': 9,\n",
       "  'hardware': 9,\n",
       "  'machine learning': 9,\n",
       "  'ai': 9,\n",
       "  'bootstrap': 9,\n",
       "  '3d max': 9,\n",
       "  'scrum': 8,\n",
       "  'analytical': 8,\n",
       "  'solidworks': 8,\n",
       "  'product': 8,\n",
       "  'jquery': 8,\n",
       "  'azure': 8,\n",
       "  'r&amp;d': 8,\n",
       "  'application support': 8,\n",
       "  'learning': 8,\n",
       "  'istqb': 7,\n",
       "  'shop drawings': 7,\n",
       "  'oop': 7,\n",
       "  'bi': 7,\n",
       "  'mvc': 7,\n",
       "  'leadership': 7,\n",
       "  'back-end': 7,\n",
       "  'design engineer': 7,\n",
       "  'react.js': 7,\n",
       "  'e-marketing': 7,\n",
       "  'abap': 7,\n",
       "  'office management': 7,\n",
       "  'training': 7,\n",
       "  'mcsa': 6,\n",
       "  'electronics': 6,\n",
       "  'startup': 6,\n",
       "  'mep': 6,\n",
       "  'application': 6,\n",
       "  'business intelligence': 6,\n",
       "  'jira': 6,\n",
       "  'backend developer': 6,\n",
       "  'mcse': 6,\n",
       "  'hse': 6,\n",
       "  'django': 6,\n",
       "  'networks': 6,\n",
       "  'banking': 6,\n",
       "  'artificial intelligence': 6,\n",
       "  'wordpress': 6,\n",
       "  'itil': 6,\n",
       "  'ui/ux': 6,\n",
       "  'program management': 6,\n",
       "  'product design': 6,\n",
       "  'commerce': 6,\n",
       "  'automation testing': 5,\n",
       "  'media': 5,\n",
       "  'network': 5,\n",
       "  'configuration': 5,\n",
       "  'senior': 5,\n",
       "  'scrum master': 5,\n",
       "  'vue.js': 5,\n",
       "  'manager': 5,\n",
       "  'troubleshooting': 5,\n",
       "  'cost control': 5,\n",
       "  'architecture engineering': 5,\n",
       "  'drawing': 5,\n",
       "  'cnc': 5,\n",
       "  'facility management': 5,\n",
       "  'technology': 5,\n",
       "  'cybersecurity': 5,\n",
       "  'digital marketing': 5,\n",
       "  'support': 5,\n",
       "  'market research': 5,\n",
       "  'data entry': 5,\n",
       "  'odoo development': 5,\n",
       "  'requirements': 5,\n",
       "  'network administration': 5,\n",
       "  'siem': 5,\n",
       "  'technician': 5,\n",
       "  'indoor sales': 5,\n",
       "  'consulting': 5,\n",
       "  'duties': 5}}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jobs_list = ['data scientist', 'software engineer']  # List of job searches\n",
    "scrape_jobs_data(jobs_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyP9OhYM9AwLUZW7GvTJJlQk",
   "include_colab_link": true,
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}