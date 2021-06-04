def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {} by {} was originally published in {} in {}.".format(title, author, original_work, publishing_date)
  return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")