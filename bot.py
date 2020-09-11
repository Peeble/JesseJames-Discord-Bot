import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

f = open("data.txt", "r")
count = float(f.read())
f.close()

bot = commands.Bot(command_prefix='!')

def writeData(value):
    f = open("data.txt", "w")
    f.write(str(count))
    f.close()


def check_if_allowed(ctx):
    if (ctx.message.author.id == 82988663528488960 or ctx.message.author.id == 165711606867558400):
        return True
    else:
        return False

@bot.command(name='count')
async def jessie_james(ctx):
    await ctx.channel.send('Jesse James count is at: ' + str(count))


@bot.command(name='jj')
async def jessie_james(ctx):
    global count

    count += 1
    writeData(count)
    await ctx.send('Jesse James count increased to: ' + str(count))

@bot.command(name='j')
async def jessie_james(ctx):
    global count

    count += 0.5
    writeData(count)
    await ctx.send('Jesse James count increased to: ' + str(count))

@bot.command(name='unj')
async def jessie_james(ctx):
    global count

    count -= 0.5
    writeData(count)
    await ctx.send('Jesse James count decreased to: ' + str(count))

@bot.command(name='unjj')
async def jessie_james(ctx):
    global count

    count -= 1
    writeData(count)
    await ctx.send('Jesse James count decreased to: ' + str(count))

@bot.command(name='reset')
@commands.check(check_if_allowed)
async def reset(ctx):
    global count
    count = 0

    writeData(count)
    await ctx.send('Jesse James count has been reset to 0')

@bot.command(name='set')
@commands.check(check_if_allowed)
async def setcount(ctx, newcount):
    if (newcount.isdigit()):
        global count
        count = float(newcount)

        writeData(count)

        await ctx.send('Jesse James count has been set to ' + str(count))
    else:
        await ctx.send('Invalid. Usage is !set <int>')

@bot.command(name='jjfacts')
async def facts(ctx):
    jj_facts = [
        'He left home when Jesse was very young to minister to gold seekers out West and died of cholera while there.',
        'Residing in Missouri, the James family owned slaves and supported the Confederacy.',
        'When Jesse was about 15, Union soldiers seeking information attacked the James household, hanging Jesse’s' \
        + ' stepfather from a tree (he survived, but with mental damage) and roughing up young Jesse.This incident' \
        + ' is believed to be the spark that led to Jesse joining the Confederate guerrillas.',
        'Before he even became an outlaw, Jesse was shot in the chest on two separate occasions.' \
        + 'Once in 1864 while trying to steal a saddle from a farmer and once the following year by Union soldiers.',
        'Jesse and other guerrillas might have slaughtered and scalped unarmed Union soldiers.',
        'Jesse was a cousin kisser. He married his first cousin Zerelda “Zee” Mimms (who was named after Jesse’s mother).',
        'His nickname was “Dingus”.He reportedly earned the nickname after shooting off the tip of his finger while' \
        + ' cleaning a pistol. Because he didn’t like to curse, he said “That’s the dod-dingus pistol I ever saw”.',
        'The James gang’s “Robin Hood” image was carefully crafted with the help of editor John Newman Edwards. He would' \
        + ' write favorable news articles with gems such as “[the James gang are] men who might have sat with Arthur at' \
        + ' the Round Table, ridden in tourney with Sir Lancelot, or won the colors of Guinevere” (Kansas City Times, 29 Sept. 1872).',
        'Jesse loved publicity, and was even known to hand out “press releases” to witnesses at the scenes of his crimes. One, which' \
        + ' exaggerates Jesse’s height, is said to have read: “The most daring robbery on record. The southbound train on the' \
        + ' Iron Mountain Railroad was stopped here this evening by five heavily armed men and robbed of ____ dollars… The robbers' \
        + ' were all large men, none of them under six feet tall. They were masked, and started in a southerly direction after they' \
        + ' had robbed the train, all mounted on fine-blooded horses. There is a hell of an excitement in this part of the country!”',
        'Despite the Robin Hood image of stealing from the rich and giving to the poor, there is no evidence that Jesse and his gang' \
        + ' ever did so.Evidence suggests they kept all of their spoils for themselves.',
        'Jesse once almost overdosed on morphine. Most agree that it was accidental, but there is speculation that it was a suicide attempt.',
        'He (or possibly one of his “colleagues”) shot a little girl while robbing the Kansas City Exposition on Sept. 26, 1872.' \
        + ' He later wrote (anonymously) in a public letter “It is true that I shot a little girl, though it was not intentional,' \
        + ' and I am very sorry that the child was shot; and if the parents will give me their address through the columns of the' \
        + ' Kansas City Weekly Times, I will send them money to pay her doctor’s bill.”',
        'He, along with his gang, robbed a stagecoach while on his honeymoon in Austin, TX, 1874. Who takes their gang on their honeymoon? Jesse James, that’s who.',
        'Jesse (and his brother) cost his mother her arm and his half-brother his life. Agents of the Pinkerton Detective Agency on' \
        + ' the hunt for Jesse and brother Frank threw an incendiary device into the family home, killing the 4-year-old half-brother and causing the mother to need her right arm amputated.',
        'Legend says Jesse jumped a 20 foot gulch on horseback while fleeing a scene, but historians say it probably never happened.' \
        + ' Most historians agree that it would be physically impossible to jump Devil’s Gulch, located in Garretson, South Dakota. Jesse probably went around it.',
        'His own pistol was used to kill him while he was tidying up his house.Bob Ford, looking for reward money, shot him in the back of the head while he was turned dusting a picture on the wall on April 3, 1882.',
        'After the murder, Bob Ford toured with a stage show reenacting the incident. It was not well-received, particularly because of the fact that he shot Jesse while his back was turned.',
        'Jesse’s son starred in two silent films about his father’s life, playing the roles of both himself and his father. Both films, “Jesse James Under the Black Flag” and “Jesse James as the Outlaw”, were filmed in 1921.',
        'After his death, Jesse’s mother charged tourists a quarter for pebbles taken from his grave.',
        'Shooter Bob Ford’s epitaph read “The man who shot Jesse James”, while Jesse’s epitaph read “In Loving Memory of my Beloved Son, Murdered by a Traitor and Coward Whose Name is not Worthy to Appear Here”.',
        'A man named J. Frank Dalton claimed to be Jesse in the late 1940s/early 50s. Everyone loves a good conspiracy theory, and some think there is compelling evidence. A DNA test proved Dalton’s claims wrong, though.',
        'He had many aliases and identities. Some known aliases included Thomas Howard, John. D. Howard, William Campbell (a Texas cattleman), and Charles Lawson “of Nottingham, England” (there is some speculation about whether or not Jesse would have been able to pull off a convincing English accent). His son Jesse James, Jr., who was led to believe that his own name was Tim Howard until after his father’s death, even recalled that Jesse sometimes walked with a cane and a limp as a disguise.',
        'He blinked. A lot. Historians think he may have had an eye condition that caused chronic inflammation, called blephartis.',
        'During his time with the guerrillas, he dressed as a young girl. From Jesse James, Jr.’s memoir: “Jesse James, dressed as a young girl, rode on horseback up to this house and called its mistress out. Imitating the' \
        + ' voice and manner of a girl my father told her that he lived not far away, that he was a girl fond of adventure, and would like to come to the house that night, bringing two or three neighbor girls, “to have a good' \
        + ' time.” The mistress of the house consented, and the supposed girl on horseback said he and the other girls would be there that night. The mistress sent word at once to the Federal officers in Independence that four' \
        + ' new girls would be at her house that night. It was after dark when Jesse James and the other guerrillas rode up to the house, and dismounting, crept up and peered in at the windows. Twelve Federal officers were in there with the women. No guards or sentinels were out. The Federals felt secure. All the company was in one room, five women and twelve men. A cheery fire blazed and crackled on the hearth of the old-fashioned fire place. Jesse James, with five men went to one window. Bill Gregg, with five men, went to another. Each of the nine guerrillas in the darkness outside selected his man. At a signal that had been agreed upon there was the crack of nine revolvers that sounded like the discharge of a single gun. The glass, slivered in a thousand bits, crashed, and nine of the Federal soldiers fell dead at that first volley. The remaining three fell dead an instant later. The guerrillas mounted and rode away.”',
        'He murdered at least 12 people, and claimed to have murdered 17.'
    ]

    response = random.choice(jj_facts)
    await ctx.send(response)


bot.run(token)