def check_content_value(test, item):
    check_dict = item.__dict__

    for value in {'name', 'text', 'category_id'}:
        test.assertIn(value, check_dict)

    test.assertIn('tags', check_dict['_prefetched_objects_cache'])

    for value in {'is_on_main', 'image', 'gallery_photo', 'is_published'}:
        test.assertNotIn(value, check_dict)
