# DiscordBot
PL:

Discordbot jest to bot do komunikatora discord wstępnie robiony był w ramach pomocy koledze 
z pisaniem jego własnego bota po zrobieniu kilku podstawowych komend został on porzucony do 
czasu gdy znowu pomagałem temu koledze z jego botem

Najważniejsze funkcje:
-Schowek
Jest to funkcja bota by zapisywał pliki wysłane mu na discordzie do folderu "schowek".
Może on zapisywać oraz wysyłać wcześniej zapisane pliki jak i tworzyć liste plików w "schowek" i wysyłania
jej na kanał na discordzie.
-Wykrywanie ruchu
Bardzo proste wykrywanie ruchu które odbywa sie poprzez uruchomienie programu "Wykrywacz ruchu"
oba programy "komunikują" się poprzez plik o nazwie "ruch".
Gdy wykrywacz wykryje ruch zmienia 0 na 1 w pliku "ruch" a sam discordbot sprawdza ten plik co kilka sekund
po zmianie 0 na 1 discordbot wysyła na konkretny kanał na discordzie wiadomość o wykryciu ruchu.

W większości ten program jest stworzony by pomóc koledze w rozwijaniu jego bota.
Ja piszę swój odpowiednik w pythonie a następnie pomagam mu "przerobić" go na język java gdyż w nim 
jest stowrzony jego bot.

ENG:

Discordbot is it a bot for communicator "Discord" initially it has been made to help a friend
in making his own bot after making few basic i throw away this project until next time i was helping my friend with his bot

Most important functions:
-Clipboard
This bot function save files send to him on discord server to directory "schowek".
He can save and send earlier saved files and sending list of files in "schowek".
-Motion detection
Basic motion detection which starts with runing program "Wykrywacz ruchu"
both programs "communicate" by file "ruch"
If this program detects motion it changes 0 to 1 in file "ruch" and DiscordBot checks this file every few seconds after change DiscordBot is sending message on special channel that motion has been detected.

In majority this program is created to help my friend develop his own.
I write in Python then help him convert it to Java.
