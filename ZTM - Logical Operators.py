is_magician = False
is_expert = True

# Check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print("you are a master magician")

# Check if magician, but not expert: "at least you are getting there"
elif is_magician and not is_expert:
    print("at least you are getting there")

# if you are not a magician: "you need magic powers"
elif not is_magician:
    print("you need magic powers")
