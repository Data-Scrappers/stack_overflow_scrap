from parses import parser, dataframe_tags, dataframe_data, tag_parse


if __name__ == '__main__':
    tags = parser()
    tags_df = dataframe_tags(tags)
    for elem in tags:
        for current_tag in elem.keys():
            for x in range(1, 2):
                csv_export = dataframe_data(
                        f'https://stackoverflow.com/questions/tagged/{current_tag}?tab=active&page={x}&pagesize=50',
                    current_tag=current_tag)
                csv_export.to_csv(f'{current_tag}.csv', index=True, sep=':', mode='a')

