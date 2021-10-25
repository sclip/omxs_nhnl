from src import defines
import discord
import asyncio

activity = discord.Game("Sending NH-NL Data")
client = discord.Client(activity=activity)
users = []


def init(payload):
	@client.event
	async def on_ready():

		for user in defines.defines["PM List"]:
			users.append(await client.fetch_user(user))

		text = f"""
			{payload}
		"""

		data_embed = discord.Embed(title="NH-NL Data", description=text, colour=discord.Colour(0x3239dc))

		for user in users:
			await user.send(embed=data_embed)

		await client.close()

	token = defines.defines["Bot Token"]
	if len(token) == 0:
		print("Invalid Token: Token must not be empty! Fix this in config.json")
		quit()

	async def client_start():
		await client.start(token)

	loop = asyncio.get_event_loop()
	coroutine = client_start()
	loop.run_until_complete(coroutine)
