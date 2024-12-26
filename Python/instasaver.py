import instaloader

ig = instaloader.Instaloader()
# ig.download_comments = False
# ig.save_metadata = False
dp = input("Enter Insta Username:")
ig.download_profile(dp, profile_pic_only=False)
