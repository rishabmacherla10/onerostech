from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def index():
	return render_template('main.html')

@app.route("/game_page", methods=['POST'])
def game_page():
	desc_list=["desc1","desc2","desc3","desc4","desc5","desc6","desc7","desc8","desc9","desc10","desc11"]
	game_icons=["word_search.png","craps_icon.png","roulette_icon.png","sicbo_icon.png","baccarat_icon.png","carribean_icon.png","crazy_4poker _icon.png","let_it_ride_icon.png","paigow_icon.png","three_card_icon.png","messesippi_icon.png"]
	game_images=["word_game_image.png","craps_image.png","roulette_image.png","sic_bo_image.png","baccarat_image.png","carribean_image.png","crazy_4-poker_image.png","let_it_ride_image.png","pai_gow_image.png","three_card_image.png","mississippi_image.png"]
	game_videos=["word_cross.mp4","craps_video.mp4","ROULETTE_VIDEO.mp4","sic_bo_video.mp4","BACCARAT.mp4","Caribbean_Stud_Poker.mp4","crazy_4_poker_video.mp4","Let_It_Ride_Poker.mp4","word_cross.mp4","Three_Card_Poker.mp4","mississippi.mp4"]
	screenshots=["ss1.png","ss2.png","ss3.png","ss4.png","ss5.png","ss6.png","ss7.png"]
	if request.method == "POST":
		btn_name=request.form['game_btn']
		if btn_name == "word" :
			screens=[]
			desc_con=desc_list[0]
			game_icon=game_icons[0]
			game_image=game_images[0]
			game_video=game_videos[0]
			fname="word cross"
			for i in range(0,6):
				screens.append(screenshots[i])
			return render_template('game_page.html',icon=game_icon,desc=desc_con,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "craps" :
			screens=[]
			desc_con=desc_list[1]
			game_icon=game_icons[1]
			game_image=game_images[1]
			game_video=game_videos[1]
			fname="craps"
			for i in range(0,6):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "roulette" :
			screens=[]
			desc_con=desc_list[2]
			game_icon=game_icons[2]
			game_image=game_images[2]
			game_video=game_videos[2]
			fname="roulette"
			for i in range(0,5):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "sicbo" :
			screens=[]
			desc_con=desc_list[3]
			game_icon=game_icons[3]
			game_image=game_images[3]
			game_video=game_videos[3]
			fname="sic bo"
			for i in range(0,6):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "baccarat" :
			screens=[]
			desc_con=desc_list[4]
			game_icon=game_icons[4]
			game_image=game_images[4]
			game_video=game_videos[4]
			fname="baccarate"
			for i in range(0,6):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "stud" :
			screens=[]
			desc_con=desc_list[5]
			game_icon=game_icons[5]
			game_image=game_images[5]
			game_video=game_videos[5]
			fname="caribbean"
			for i in range(0,6):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "crazy" :
			screens=[]
			desc_con=desc_list[6]
			game_icon=game_icons[6]
			game_image=game_images[6]
			game_video=game_videos[6]
			fname="crazy 4 poker"
			for i in range(0,5):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "ride" :
			screens=[]
			desc_con=desc_list[7]
			game_icon=game_icons[7]
			game_image=game_images[7]
			game_video=game_videos[7]
			fname="let it ride"
			for i in range(0,7):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "pai" :
			screens=[]
			desc_con=desc_list[8]
			game_icon=game_icons[8]
			game_image=game_images[8]
			game_video=game_videos[8]
			fname="paigow"
			for i in range(0,5):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)	
		elif btn_name == "three" :
			screens=[]
			desc_con=desc_list[9]
			game_icon=game_icons[9]
			game_image=game_images[9]
			game_video=game_videos[9]
			fname="three card poker"
			for i in range(0,7):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		elif btn_name == "mississippi" :
			screens=[]
			desc_con=desc_list[10]
			game_icon=game_icons[10]
			game_image=game_images[10]
			game_video=game_videos[10]
			fname="mississippi"
			for i in range(0,6):
				screens.append(screenshots[i])
			return render_template('game_page.html',desc=desc_con,icon=game_icon,image=game_image,video=game_video,ss=screens,folder=fname)
		return render_template('main.html')
	return render_template("main.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

# @app.route("/game")
# def game():
#     return render_template('game.html')

@app.route("/privacy")
def pp():
	return render_template('privacy.html')

if __name__ == "__main__":
	app.run(debug=True)
