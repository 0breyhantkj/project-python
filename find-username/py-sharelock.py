""" Peoject Sederhana Search Username Social Media """

import requests

url = {
	"tiktok": "https://www.tiktok.com/@",
	"instagram": "https://www.instagram.com/",
	"x": "https://x.com/",
	"facebook": "https://www.facebook.com/",
	"youtube": "https://www.youtube.com/@",
	"reddit": "https://www.reddit.com/user/",
	"threads": "https://www.threads.net/@",
	"pinterest": "https://www.pinterest.com/",
	"snapchat": "https://www.snapchat.com/add/",
	"github": "https://github.com/",
	"linkedin": "https://www.linkedin.com/in/",
	"telegram": "https://t.me/",
	"bluesky": "https://bsky.app/profile/",
	"twitch": "https://www.twitch.tv/"
}

print(f"""

	/////////////////////////////////
	///////  ///////////////   //////
	///       /////////////   ///////
	//   /////////////////   ////////
	//    ///////////////   /////////
	////   /////////////   //////////
	///////   /////////   ///////////
	//////    ////////   ////////////
	//     //////////              //
	/////////////////////////////////
	      [ serlok tak parani ]
""")
username = input("\n\nMasukan nama target: ")

for social_media, base_url in url.items():
	fullurl = base_url + username

	try:
		response = requests.get(fullurl)
		if response.status_code == 200:
			print(f"{social_media} -> {fullurl}")
		else:
			print(f"{social_media} -> not found")
	except requests.exceptions.RequestException as e:
	   	 print(f"Terjadi error saat mengakses URL: {e}")
