import pyperclip
import os
import platform
import secrets
from termcolor import colored
plat= platform.platform()
if(plat=='Windows'):
    clear_command= 'cls'
else:
    clear_command= 'clear'
os.system(clear_command)
print('Just choose things the right way. I am too lazy to code out extra cases at this point')
def menu():
    var= int(input('''Choose what to copy:
[1.] Shrug ¯\_(ツ)_/¯                                [2.] Lenny face ( ͡° ͜ʖ ͡°)
[3.] Bear ʕ•ᴥ•ʔ                                      [4.] Gun guy1 ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿
[5.] Fight! (ง ͠° ͟ل͜ ͡°)ง                               [6.] Huh (▀̿Ĺ̯▀̿ ̿)
[7.] Lenny faces ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)             [8.] Kawai1 ༼ つ ◕_◕ ༽つ
[9.] Kawai1 (づ｡◕‿‿◕｡)づ                             [10.] End me ಠ_ಠ
[11.] Old guy ( ͡°╭͜ʖ╮͡° )                              [12.] End me2 (ಥ﹏ಥ)
[13.] Over enthusiastic pointing (☞ﾟ∀ﾟ)☞             [14.] Doggo (ᵔᴥᵔ)
[15.] Gun guy 2 ̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿                 [16.] Good day ♪~ ᕕ(ᐛ)ᕗ
[17.] Love ♥‿♥                                       [18.] End me3 ◉_◉              
[19.] Weird smile ༼ʘ̚ل͜ʘ̚༽                              [20.] Strong ᕦ(ò_óˇ)ᕤ
[21.] Over Enthusiastic pointing2 ☜(˚▽˚)☞            [22.] Innocent smile ˙ ͜ʟ˙
[23.] Innocent yet dangerous (ง°ل͜°)ง                 [24.]  Mayhem （╯°□°）╯︵( .o.)
[25.] Irdk ┬──┬ ノ( ゜-゜ノ)                         [26.] Kill me3 ಠ⌣ಠ]
[27.] Necrophilic murderer ლ(´ڡ`ლ)                   [28.] Kawai3 ｡◕‿‿◕｡
[29.] Kawai_end me (─‿‿─)                            [30.] Sweating (；一_一)
[31.] Retarded Shrug ¯\(°_o)/¯                       [32.] Butterfly Ƹ̵̡Ӝ̵̨̄Ʒ       
[33.] Blushing (▰˘◡˘▰)                               [34.] Kawai4 ◔ ⌣ ◔
[35.] Kawai_confused ◔̯◔                              [36.] Angry Cyka Blyat ｡゜(｀Д´)゜｡
[37.] Surprised Cyka Blyat °Д°                       [38.]Cute swag 〆(・∀・＠)
[39.] Happy ^̮^                                       [40.] Emo (･.◤)
[41.] Flirty end me ಠ‿↼                              [42.] Crying end me ಠ_ಥ
'''))
    if(var==1):
        pyperclip.copy('¯\_(ツ)_/¯')
    elif(var==2):
        pyperclip.copy('( ͡° ͜ʖ ͡°)')
    elif(var==3):
        pyperclip.copy('ʕ•ᴥ•ʔ')
    elif(var==4):
        pyperclip.copy(" ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿")
    elif(var==5):
        pyperclip.copy("(ง ͠° ͟ل͜ ͡°)ง")
    elif(var==6):
        pyperclip.copy('(▀̿Ĺ̯▀̿ ̿)')
    elif(var==7):
        pyperclip.copy('( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)')
    elif(var==8):
        pyperclip.copy("༼ つ ◕_◕ ༽つ")
    elif(var==9):
        pyperclip.copy("(づ｡◕‿‿◕｡)づ")
    elif(var==10):
        pyperclip.copy('ಠ_ಠ')
    elif(var==11):
        pyperclip.copy('( ͡°╭͜ʖ╮͡° )')
    elif(var==12):
        pyperclip.copy('(ಥ﹏ಥ)')
    elif(var==13):
        pyperclip.copy("(☞ﾟ∀ﾟ)☞")
    elif(var==14):
        pyperclip.copy("(ᵔᴥᵔ)")
    elif(var==15):
        pyperclip.copy(" ̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿")
    elif(var==16):
        pyperclip.copy('♪~ ᕕ(ᐛ)ᕗ')
    elif(var==17):
        pyperclip.copy("♥‿♥")
    elif(var==18):
        pyperclip.copy("(◉_◉") #
    elif(var==19):
        pyperclip.copy('༼ʘ̚ل͜ʘ̚༽')
    elif(var==20):
        pyperclip.copy("ᕦ(ò_óˇ)ᕤ")
    elif(var==21):
        pyperclip.copy("☜(˚▽˚)☞")
    elif(var==22):
        pyperclip.copy("˙ ͜ʟ˙")
    elif(var==23):
        pyperclip.copy('(ง°ل͜°)ง')
    elif(var==24):
        pyperclip.copy('（╯°□°）╯︵( .o.))')
    elif(var==25):
        pyperclip.copy("┬──┬ ノ( ゜-゜ノ)")
    elif(var==26):
        pyperclip.copy("ಠ⌣ಠ")
    elif(var==27):
        pyperclip.copy('ლ(´ڡ`ლ)')
    elif(var==28):
        pyperclip.copy('｡◕‿‿◕｡')
    elif(var==29):
        pyperclip.copy('(─‿‿─)')
    elif(var==30):
        pyperclip.copy("(；一_一)")
    elif(var==31):
        pyperclip.copy("¯\(°_o)/¯")#
    elif(var==32):
        pyperclip.copy("Ƹ̵̡Ӝ̵̨̄Ʒ")
    elif(var==33):
        pyperclip.copy('(▰˘◡˘▰)')#
    elif(var==34):
        pyperclip.copy("◔ ⌣ ◔")#
    elif(var==35):
        pyperclip.copy("◔̯◔")#
    elif(var==36):
        pyperclip.copy("｡゜(｀Д´)゜｡")##
    elif(var==37):
        pyperclip.copy("°Д°")
    elif(var==38):
        pyperclip.copy('〆(・∀・＠)')#
    elif(var==39):
        pyperclip.copy("^̮^")#
    elif(var==40):
        pyperclip.copy("･.◤)")#
    elif(var==41):
        pyperclip.copy('ಠ‿↼')
    elif(var==42):
        pyperclip.copy('ಠ_ಥ')
while(1==1):
    os.system(clear_command)
    menu()
    print('copied!')
