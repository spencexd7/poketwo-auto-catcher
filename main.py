# project info

# author : https://github.com/spencexd7
# discord : https://discord.gg/gpqMWg5PAY


import discord
from discord.ext import commands

token = ""

client = commands.Bot(command_prefix='autocatch')

client._skip_check = lambda x, y: False


@client.event
async def on_message(message):

  def check(m):
    return m.channel == message.channel and m.author != client.user and "The pokémon is" in m.content

  global hint
  embeds = message.embeds
  if not embeds:
    await client.process_commands(message)
    return
  title = embeds[0].to_dict().get('title')

  if "pokémon has appeared" in title.lower():
    hint = ""
    response = await wait_for_response("<@716390085896962058> h", message.channel, check)
    if "The pokémon is" in response.content:
      s = response.content.split(" is ")[1].replace(".", "")
      x = get(s)
      if x:
        best_match = max(x,
                         key=lambda i: sum(1 for c in s
                                           if c.lower() in i.lower()))
        await send(f"<@716390085896962058> c {best_match}", message.channel)
      else:
        await send("No matches found", message.channel)


async def wait_for_response(message, channel, check):
  await channel.send(message)
  response = await client.wait_for('message', check=check, timeout=60)
  return response


async def send(message, channel):
  await channel.send(message)


def get(val):
  val = val.lower()
  while "\_" in val:
      val = val.replace("\_", "-")
  length = len(val)
  l = list(val)
  
  
  with open('pokes.txt') as f:
         lines = [line.rstrip() for line in f]
        
  new_names = []
  for i in lines:
    if len(i) == length:
      new_names.append(i)
  final_list = []
  for i in new_names:
    name_list = list(i)
    index = 0
    flag = False
    for k in l:
      if name_list[index] != k and k != "-":
        flag = True
      index = index+1
    if not flag:
      final_list.append(i)
  return final_list


client.run(token)
