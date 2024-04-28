## Bitwarden Vault Export Script
This script manually exports names, passwords and websites of Bitwarden vault items in the Bitwarden macOS app. It's based on Apple Script and is written really really badly.
You have to be logged into Bitwarden and it has to be unlocked (e.g. by using fingerprint).
It's not meant as a perfect portable script, but merely as a proof of concept for hopeless people, to provide an example template to use to recover passwords.
It requires exact coordinates of some buttons that are located in the Bitwarden macOS application.
Also, it's currently only optimized for German keyboards, as I used keycodes (which you shouldn't do, for the sake of portability).

### Prerequisites
- Apple Script Editor (Standard software on macOS)
- Bitwarden macOS App (https://apps.apple.com/de/app/bitwarden/id1352778147?mt=12)
- https://github.com/BlueM/cliclick (available via homebrew)

### Why?
I use Bitwarden as my primary password manager. Recently I got hacked, and all my Bitwarden passwords (probably by extracting them from the RAM, idk) got stolen. I changed the password to a random passphrase, wrote it down to a piece of paper, but lost the paper. Now I was left with a working Bitwarden vault (I enabled the login via fingerprint on macOS and Face ID on iOS), but without the master password. Talked to the Bitwarden support, and they told me that I can't do anything, as the vault is encrypted with the master password.

But obviously, as I am still logged in via macOS app, I could still go through the passwords one by one and copy them. This is also stated [here](https://bitwarden.com/help/forgot-master-password/). 

So I tried to do it via an Auto Clicker. Unfortunately I didn't find any good software for macOS - I am familiar with AutoIt on Windows (from my browsergame days), but that's not available for macOS. But by some Googling around I found out that I could solve my problem with Apple Script. I have never used it, any afaik it's more legacy then a current option, but it worked.

### Why cliclick?
While Apple Script can do non-context clicks, they don't act as normal clicks, like the ones that you do manually. For example, they don't actually move your mouse. Also you can't do double click.
cliclick is needed for two purposes. The first is the focusing of a specific area of the Bitwarden app. This needs to be focused, so that the Arrow down keycode works. This wouldn't work with Apple Scripts clicks.
Second one is a triple click, that is needed to copy the name of the password item. Probably it's possible somehow with Apple Script, but I was too lazy to find a way.

### Usage
#### Setting the coordinates
I've labelled the click coords with comments:
| coordinates | button |
|-----|------|
|{xxx,yyy}|copy button next to the password |
You need to manually find the coordinates. You can do this by using the macOS-integrated Screenshot tool (it's actually just called "Screenshot"). Select the "select area on screen" option, and then put the rectangle to the upper left part of the screen, right to the top-left edge. Now, by moving the bottom-right edge you can find out the coordinates of the respective buttons, displayed just at that edge (in the format `(XXXxYYY)`).
#### Running the program
After changing the coordinates, you should be ready to go. The script needs the Bitwarden app to be opened, on the default vault screen (that's the screen that pops up when you start the app). You should decrypt the vault by fingerprint, Face ID, or whatever. Next, also start TextEdit, set the text mode (via View -> Plain Text) to plain text. Afterwards, you should be ready to start the script. If it doesn't work, you maybe need to implement some delays or extend the main delay at the start of the script (default is about 1.3 seconds, to make sure that the overlay messages that pop up when you copy the password disappear in time).

While debugging and making clear that the script runs, make sure to set the loop amount very low, and/or set the main delay very high, so that you've got time to stop the scripts in between the cycles.