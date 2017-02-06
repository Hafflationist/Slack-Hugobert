import time

import numpy as MatheBib
from slackclient import SlackClient

token = "xoxb-137313719123-2M5Unu8b7x7BXvwQi9exTyeK"

sc = SlackClient(token)


def NormalenformEbene(S1, S2, S3, R11, R12, R13, R21, R22, R23):
    Stützvektor = MatheBib.array([S1, S2, S3])
    Richtungsvektor1 = MatheBib.array([R11, R12, R13])
    Richtungsvektor2 = MatheBib.array([R21, R22, R23])

    Kreuzvektor = MatheBib.cross(Richtungsvektor1, Richtungsvektor2)
    K = Stützvektor[0] * Kreuzvektor[0] + Stützvektor[1] * Kreuzvektor[1] + Stützvektor[2] * Kreuzvektor[2]

    return "E:x =\t" + str(Kreuzvektor[0]) + "x₁ + " + str(Kreuzvektor[1]) + "x₂ + " + str(Kreuzvektor[2]) + "x₃ = " + str(K)


def getUserName(id):
    userinfo = userinfo = sc.api_call(
        "users.info",
        user=str(id)
    )

    return userinfo.get("user").get("name")


if sc.rtm_connect():

    sc.api_call(
        "chat.postMessage",
        channel="@U40LJ3SDP",
        text="Hi :tada:",
        as_user=True
    )

    while True:
        for slackmessage in sc.rtm_read():
            if slackmessage is not None:
                user = slackmessage.get("user")
                text = slackmessage.get("text")
                if user is not None and text is not None:
                    print(user + " -> " + text)
                    if text == "Hi":
                        username = getUserName(user)
                        print(username)
                        sc.api_call(
                            "chat.postMessage",
                            channel="@" + username,
                            text="Hi :tada:",
                            as_user=True
                        )
                    if text.startswith("!"):
                        if text == "!help":
                            username = getUserName(user)
                            print(username)
                            sc.api_call(
                                "chat.postMessage",
                                channel="@" + username,
                                text="Hi " + username + " :tada:\nHier eine Liste der BEFEHLE: \n!help        -        Zeigt dir diese Hilfe an\n\nMehr folgt!",
                                as_user=True
                            )
                        if "normalform" in text.lower():
                            argumente = text.split(" ")[1]
                            vektoren = argumente.split(".")

                            if len(vektoren) is not 9:
                                username = getUserName(user)
                                print(username)
                                sc.api_call(
                                    "chat.postMessage",
                                    channel="@" + username,
                                    text="Deine Argumente sind falsch. Benutze !normalform s1.s2.s3.r11.r12.r13.r21.r22.r23 :tada:",
                                    as_user=True)
                            else:
                                username = getUserName(user)
                                print(username)
                                sc.api_call(
                                    "chat.postMessage",
                                    channel="@" + username,
                                    text="Die Lösung: \n" + NormalenformEbene(int(vektoren[0]), int(vektoren[1]), int(vektoren[2]), int(vektoren[3]), int(vektoren[4]), int(vektoren[5]), int(vektoren[6]), int(vektoren[7]), int(vektoren[8])),
                                    as_user=True)



        time.sleep(1)
# while True:
#     sc.api_call(
#         "chat.postMessage",
#         channel="@sophia",
#         text="Testnachricht :tada:",
#         as_user=True
#     )
#
#
#
#
#     NormalenformEbene(int(input("Stützvektor\t1:\t")), int(input("Stützvektor\t2:\t")), int(input("Stützvektor\t3:\t")),
#                       int(input("Richtungsvektor1\t1:\t")), int(input("Richtungsvektor1\t2:\t")), int(input("Richtungsvektor1\t3:\t")),
#                       int(input("Richtungsvektor2\t1:\t")), int(input("Richtungsvektor2\t2:\t")), int(input("Richtungsvektor2\t3:\t")))
#     Stützvektor = MatheBib.array([int(input("Stützvektor\t1:\t")), int(input("Stützvektor\t2:\t")), int(input("Stützvektor\t3:\t"))])
#     Richtungsvektor1 = MatheBib.array([int(input("Richtungsvektor1\t1:\t")), int(input("Richtungsvektor1\t2:\t")), int(input("Richtungsvektor1\t3:\t"))])
#     Richtungsvektor2 = MatheBib.array([int(input("Richtungsvektor2\t1:\t")), int(input("Richtungsvektor2\t2:\t")), int(input("Richtungsvektor2\t3:\t"))])
#
#     Kreuzvektor = MatheBib.cross(Richtungsvektor1, Richtungsvektor2)
#     K = Stützvektor[0] * Kreuzvektor[0] + Stützvektor[1] * Kreuzvektor[1] + Stützvektor[2] * Kreuzvektor[2]
#
#     print("E:x =\t" + str(Kreuzvektor[0]) + "x₁ + " + str(Kreuzvektor[1]) + "x₂ + " + str(Kreuzvektor[2]) + "x₃ = " + str(K))
#
#
