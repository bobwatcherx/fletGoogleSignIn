from flet import *
from flet.auth.providers.google_oauth_provider import GoogleOAuthProvider




clientID = "1029569400250-p3j0j4eedbic8jcbu3h6k4cjjhk3kk95.apps.googleusercontent.com"
clientSecret = "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"
def main(page:Page):

	provider = GoogleOAuthProvider(
		client_id = clientID,
		client_secret = clientSecret,
		redirect_url="http://localhost:8550/api/oauth/redirect"

		)

	resulttxt = Column()

	def logingoogle(e):
		page.login(provider)


	# AND AFTER LOGIN SUCCESS > YOU CAN GET INFORMATION ACCOUNT
	# FROM USER LOGIN GOOGLE
	# LIKE EMAIL
	# LIKE USERNAME, ACCESS TOKEN , AND MORE

	def on_login(e):
		print(page.auth.user)

		# AND SHOW INFORMATION ABOUT USER IN SCREEN APP
		resulttxt.controls.append(
			Column([
				Text(f"name : {page.auth.user['name']}"),
				Text(f"email : {page.auth.user['email']}"),
				Text(f"access token : {page.auth.token.access_token}"),
				Text(f"id: {page.auth.user.id}")

				])

			)
		page.update()


	# AND NOW REGISTER LISTENING FUNCTION
	page.on_login = on_login

	page.add(
		Column([
			Text("Login GOogle",size=30),

		ElevatedButton("Sign google",
			bgcolor="blue",color="white",
			on_click=logingoogle

			),
		resulttxt
			])

		)
flet.app(target=main,port=8550,view=WEB_BROWSER)
