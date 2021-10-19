import os
import uuid
from parses import parse_tags, parse_questions

# Every page contains 50 questions.
# @ref QUESTION_PAGES * 50 records will be
# in tag csv file
QUESTION_PAGES = 500
# Each page with tags contains 36 tags.
# For every tag @ref QUESTION_PAGES will be parsed
TAGS_PAGES = 100
# Directory to which output csv files will be generated
DATA_DIRECTORY = 'data_' + str(uuid.uuid4())


def write_to_csv_questions_for_tag(tag, directory, pages_to_parse=QUESTION_PAGES):
    for x in range(1, pages_to_parse + 1):
        csv_export = parse_questions(x, current_tag=tag)
        csv_export.to_csv(f'{directory}/{tag}.csv', index=True, sep=':', mode='a')


if __name__ == '__main__':
    data_directory = DATA_DIRECTORY
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    for page in range(1, TAGS_PAGES + 1):
        print("Start parsing page {}/{} of tags".format(page, TAGS_PAGES))
        tags_df = parse_tags(page)
        tags_df.to_csv(f'{data_directory}/all_tags.csv', index=True, sep=':', mode='a')

        for current_tag in tags_df['tags']:
            print("Start parsing {} tag".format(current_tag))
            write_to_csv_questions_for_tag(current_tag, data_directory)

    print("Data generation is finished, check {} repository".format(data_directory))
