from meme_engine.meme_creator import MemeEngine

if __name__ == "__main__":
    meme = MemeEngine("./_data/photos/dog")
    path = meme.make_meme('./_data/photos/dog/xander_1.jpg', 'The best quote ever', 'Dr. Bob')
    a = 10
