# Tatu Lehtola 2024
# hommmaa raspberry tai hostaa botti killan serverillä | vaihtoehtoisesti voi myös kysyä clearlyltä hostaisko se
# known issues: if one dude gets 2 wings in a row program bugs out and doesnt respect the ratio order anymore
# indexes: player = 0, wings = 1, kills = 2, ratio = 3
# next objective: writing data to file
# future objectives: database writing and fetching, UI, discord UI
# need big list of example players done and start testing with that, check for duplicates when adding to file
# change player creation to write to .txt file instead of array within program memory and work forward from there
# UI needs a search bar for players, Select team and list of players as default screen, a tab for how many wings and stuff

# Saman henkilön pystyy lisäämään kahdesti kunhan ei lisää peräkkäisillä komennoilla, KORJAA!!!
# jos arrayssa on 3 tyyppiä ja antaa siivet silloin kun line43 on if x == printer: niin sanoo että player not present
# jos sen antaa olla noin niin se ei sitten näytä virheviestiä isommalla arraylla kun syöttää väärän nimen

import sys
import tkinter as tk

array = []
group_comp = []

# new player creation to array
def new_player():
    player = input("Give player name: ")
    wings = int(0)
    kills = int(0)
    wing_ratio = float(0)
    array.append([player,wings,kills,wing_ratio])

# adds wings to to a player in the array
def add_mount():
    i=0
    state = 0
    while i < len(array):
        while state == 0:
            player = input("Who got wings? Leave blank if wipe. : ")
            #checks if the player name written is in the group
            for x in range(len(group_comp)):
                if group_comp[x] == player:
                    state = 1
                elif player == "":
                    state = 2
                else:
                    printer = int(len(group_comp))
                    if x == printer:
                        print("Player not present.")
        if state == 2:
                return
        if array[i][0] == player:
            array[i][1] += 1
            print("One pair of wings added.")
            i+=1
            break
        else:
            i+=1
    #adds kills to players who were present in the run
    for x in range(len(array)):
            for y in range(len(array)):
                try:
                    if group_comp[x] == array[y][0]:
                        array[y][2] += 1
                except IndexError:
                    continue

# determines who gets the next wings of the architect mount
def next_wings():
    wings_to = array[0][0]
    wings_order = []
    #calculates wings ratio
    for x in range(len(array)):
        try:
            array[x][3] = array[x][1] / array[x][2]
        except ZeroDivisionError:
            array[x][3] = 0
    #checks if there's someone with zero wing ratio
    for x in range(len(array)):
        if array[x][3] == 0:#testissä for loopin x muuttujan käyttäminen
            print("Next wings to: {}\n".format(array[x][0]))
            return
    #assigns next wings according to wings ratio
    for x in range(len(array)):
        for y in range(len(array)):
            if array[x][3] < array[y][3]:
                wings_order.append(array[x][0])
                wings_to = wings_order[0]
                print("Next wings to: {}\n".format(wings_to))
            else:
                print("Free for all.")
                return

# makes the group for current session | members need to be in original player array to be accepted
def group_members():
    print("Select group members...")
    for x in range(len(array)):
        print("{}".format(array[x][0]))
    j=0
    while len(group_comp) < 3:
        no_member = 0
        member = str(input("Give member name: "))
        for y in range(len(array)):
            if array[y][0] == member:
                print("Found player.")
                no_member = 1
                group_comp.append(member)
        if no_member == 0:
            print("No such member.")
        for x in range(len(group_comp)):
            try:
                if group_comp[x] == group_comp[x+1]:
                    del group_comp[x]
            except IndexError:
                continue
    print("Group makeup set:")

# clears current group
def clear_group():
    group_comp.clear()

def delete_player():
    player_deletion = str(input("Give name of player to delete: "))
    if player_deletion:
        for x in range(len(array)):
            print(x)
            try:
                if array[x][0] == player_deletion:
                    del array[x]
                    break
            except IndexError:
                continue


def main():
    print("Starting...")
    while True:
        i=0 
        user_input = input("add players? Leave blank to cont. Type exit to exit. : ")
        if user_input == "exit":
            break
        if user_input == "yes":
            while True:
                try:
                    iterations = input("Hom many players to add? ")
                    while i < int(iterations):
                        new_player()
                        i+=1
                    break
                except ValueError:
                    print("invalid input\n")
        if user_input == "":
            group_members()
            next_wings()
            add_mount()
            for x in range(len(array)):
                print("{}: wings: {}, kills: {}, wing_ratio: {}".format(array[x][0],array[x][1],array[x][2],array[x][3]))
            clear_group()
            delete_player()

main()
