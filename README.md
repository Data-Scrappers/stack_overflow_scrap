# Stack Overflow Questions Dataset
> DataScrappers team datathon results
---

Following repository contains Data Set collected from Stack Overflow  (https://stackoverflow.com/)
and script used for data collection.

## Script usage

Generate csv files for selected tags:
```bash
python3 main.py --tags python powerquery c++ r keras beautifulsoup
```

Generate csv files for all tags from first 5 tags pages (https://stackoverflow.com/tags):
```bash
python3 main.py --tags_pages 5
```

Generate csv files for all tags from first 5 tags pages (https://stackoverflow.com/tags).
Parse 50 question pages for every tags (there is 50 questions per page):
```bash
python3 main.py --questions_pages 50
```

## Data description

[Data folder](./data)

Collected data stored in .csv format.
Each csv file contains information about one tag, which matches file name.
Values are split by ':' delimiter.

Source example: https://stackoverflow.com/questions/tagged/python?tab=newest&page=5&pagesize=50

Record example:

|   | tag | id     | vote | answer | views | accepted |
|---|-----|--------|------|--------|-------|----------|
|0  |git  |69640112|0     |0       |5      |False     |

* tag - name of tag
* id - question id
* vote - number of votes - how the community indicates which questions and answers are most useful and appropriate
* answer - how many answers
* views - how many users saw the question
* accepted - indicates if question has accepted answer or not

[![Question Example](https://github.com/Data-Scrappers/stack_overflow_scrap/blob/main/doc_images/question_example.png)]

## Example visualization


