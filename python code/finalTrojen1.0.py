import threading
import time
def thredingGame():
    global loop_1

    import pygame
    import random

    # initialize the pygame
    pygame.init()

    # creating window
    screen = pygame.display.set_mode((600, 600))

    # change title
    pygame.display.set_caption("Space Invaders")
    # add icon
    icon = pygame.image.load('spaceship.png')
    pygame.display.set_icon(icon)

    # add background
    background = pygame.image.load('background2.jpg')

    # add player
    playerImage = pygame.image.load('spaceship.png')
    playerX = 295
    playerY = 400
    playerX_change = 0

    def player():
        # adding the icon on window
        screen.blit(playerImage, (playerX, playerY))

    # add enemy
    enemyImage = pygame.image.load('enemy.png')
    enemyY = 125
    enemyX = random.randint(0, 570)
    countX = 1
    countY = 1

    enemy2Y = 20
    enemy2X = random.randint(0, 570)
    count2X = 1
    count2Y = 1

    enemy3Y = 0
    enemy3X = random.randint(500, 570)
    count3X = 1
    count3Y = 1

    enemy4Y = 0
    enemy4X = random.randint(200, 400)
    count4X = 1
    count4Y = 1

    def enemy():
        screen.blit(enemyImage, (enemyX, enemyY))

    def enemy2():
        screen.blit(enemyImage, (enemy2X, enemy2Y))

    def enemy3(enemy3X, enemy3Y):
        screen.blit(enemyImage, (enemy3X, enemy3Y))

    # add bullet
    bulletImage = pygame.image.load('bullet.png')
    bulletY = 400
    bulletX = 295
    bulletState = 0

    def bullet():
        screen.blit(bulletImage, (bulletX, bulletY))

    # add score
    score = 0
    fontSize = 20
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    textX = 0
    textY = 0
    text = "Score : "

    def showScore(textX, textY, fontSize, text):
        scoreRender = font.render(text + str(score), True, (255, 255, 255))
        screen.blit(scoreRender, (textX, textY))

    scoreBoard = True
    running = True
    main = True
    while main:
        # game loop to run the game(run time)

        while running:
            textX = 0
            textY = 0
            # add the colour
            screen.fill((10, 105, 255))
            # adding background image
            # screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main = False
                    scoreBoard = False
                    loop_1 = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_change -= 0.1
                    if event.key == pygame.K_RIGHT:
                        playerX_change += 0.1
                    if event.key == pygame.K_SPACE:
                        bulletState = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_change = 0
                    if event.key == pygame.K_SPACE:
                        bulletState = 2

            # for score
            showScore(textX, textY, fontSize, text)

            # for bullet
            if bulletState == 0:
                bulletX = playerX
                bulletY = playerY
            if bulletY < -5 and bulletState == 2:
                bulletState = 0
            elif bulletState == 1 or bulletState == 2:
                bulletY -= 0.5
            bullet()

            playerX += playerX_change
            player()

            # for enemy1
            if 560 < enemyX <= 570:
                countX = 1
            elif 0 <= enemyX < 10:
                countX = 0

            if countX == 0:
                # enemyY += 0.3
                enemyX += 0.08
            elif countX == 1:
                # enemyY -= 0.3
                enemyX -= 0.08

            if 560 < enemyY <= 570:
                countY = 1
            elif 100 <= enemyY < 120:
                countY = 0

            if countY == 0:
                # enemyY += 0.3
                enemyY += 0.08
            elif countY == 1:
                # enemyY -= 0.3
                enemyY -= 0.08

            # for enemy2
            if 560 < enemy2X <= 570:
                count2X = 1
                enemy2Y += 10
            elif 0 <= enemy2X < 10:
                count2X = 0
                enemy2Y += 10

            if count2X == 0:
                enemy2X += 0.3
            elif count2X == 1:
                enemy2X -= 0.3

            if enemy2Y > 600:
                enemy2Y = 30

            # for enemy3
            if 560 < enemy3X <= 570:
                count3X = 1
            elif 0 <= enemy3X < 10:
                count3X = 0

            if count3X == 0:
                enemy3X += 0.08
            elif count3X == 1:
                enemy3X -= 0.08

            if 300 < enemy3Y <= 310:
                count3Y = 1
            elif 0 <= enemy3Y < 10:
                count3Y = 0

            if count3Y == 0:
                enemy3Y += 0.08
            elif count3Y == 1:
                enemy3Y -= 0.08

            # for enemy4
            if 560 < enemy4X <= 570:
                count4X = 1
            elif 0 <= enemy4X < 10:
                count4X = 0

            if count4X == 0:
                enemy4X += 0.08
            elif count4X == 1:
                enemy4X -= 0.08

            if 430 < enemy4Y <= 450:
                count4Y = 1
            elif 0 <= enemy4Y < 10:
                count4Y = 0

            if count4Y == 0:
                enemy4Y += 0.08
            elif count4Y == 1:
                enemy4Y -= 0.08

            enemy()
            enemy2()
            enemy3(enemy3X, enemy3Y)
            enemy3(enemy4X, enemy4Y)

            # game end
            if playerX - 10 <= enemyX <= playerX + 15 and playerY - 15 <= enemyY <= playerY + 15:
                running = False
                playerX_change = 0
                playerX = 295
                playerY = 400
                scoreBoard = True
            elif playerX - 10 <= enemy2X <= playerX + 15 and playerY - 15 <= enemy2Y <= playerY + 15:
                running = False
                playerX_change = 0
                playerX = 295
                playerY = 400
                scoreBoard = True
            elif playerX - 10 <= enemy3X <= playerX + 15 and playerY - 15 <= enemy3Y <= playerY + 15:
                running = False
                playerX_change = 0
                playerX = 295
                playerY = 400
                scoreBoard = True
            elif playerX - 10 <= enemy4X <= playerX + 15 and playerY - 15 <= enemy4Y <= playerY + 15:
                running = False
                playerX_change = 0
                playerX = 295
                playerY = 400
                scoreBoard = True

            # enemy killing
            if bulletX - 5 < enemyX < bulletX + 8 and bulletY - 5 < enemyY < bulletY + 8:
                enemyX = random.randint(50, 570)
                enemyY = 0
                score += 5
            if bulletX - 5 < enemy2X < bulletX + 8 and bulletY - 5 < enemy2Y < bulletY + 8:
                enemy2X = random.randint(50, 570)
                enemy2Y = 0
                score += 5
            if bulletX - 5 < enemy3X < bulletX + 8 and bulletY - 5 < enemy3Y < bulletY + 8:
                enemy3X = random.randint(50, 570)
                enemy3Y = 0
                score += 5
            if bulletX - 5 < enemy4X < bulletX + 8 and bulletY - 5 < enemy4Y < bulletY + 8:
                enemy4X = random.randint(50, 570)
                enemy4Y = 0
                score += 5

            # to update the window screen
            pygame.display.update()

        text3X = 190
        text3Y = 250
        text3 = "Game over...  "

        def showScore2(text3X, text3Y, fontSize, text3):
            scoreRender = font.render(text3, True, (255, 255, 255))
            screen.blit(scoreRender, (text3X, text3Y))

        textX = 190
        textY = 275
        text = "score: "

        text2X = 190
        text2Y = 390
        text2 = "Press Enter to play again..."

        def showScore2(text2X, text2Y, fontSize, text2):
            scoreRender = font.render(text2, True, (255, 255, 255))
            screen.blit(scoreRender, (text2X, text2Y))

        test = False

        while scoreBoard:
            # add the colour
            screen.fill((200, 10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    scoreBoard = False
                    main = False
                    loop_1 = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_KP_ENTER:
                        scoreBoard = False
                        running = True
                        main = True
                        # restarting variables //////////////////////////////
                        # player
                        playerX = 295
                        playerY = 400
                        playerX_change = 0

                        # enemy
                        enemyY = 125
                        enemyX = random.randint(0, 570)
                        countX = 1
                        countY = 1

                        enemy2Y = 20
                        enemy2X = random.randint(0, 570)
                        count2X = 1
                        count2Y = 1

                        enemy3Y = 0
                        enemy3X = random.randint(500, 570)
                        count3X = 1
                        count3Y = 1

                        enemy4Y = 0
                        enemy4X = random.randint(200, 400)
                        count4X = 1
                        count4Y = 1

                        # bullet
                        bulletY = 400
                        bulletX = 295
                        bulletState = 0

                        # score
                        score = 0
                        fontSize = 20
                        textX = 0
                        textY = 0
                        text = "Score : "
                        # //////////////////////////////////////////////////

            showScore(textX, textY, fontSize, text)
            showScore2(text3X, text3Y, fontSize, text3)
            showScore2(text2X, text2Y, fontSize, text2)

            # to update the window screen
            pygame.display.update()


#///////////////////////////////////////////////////////////////////////////////////////////////////

def thredingTrojen():
    global loop_1

    # libraries to send data to db
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    # webdriver-managers for multiple browsers
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService

    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.edge.options import Options as EdgeOptions

    # checking the network connection
    import platform
    import subprocess

    def ping_host(host="8.8.8.8"):
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", host]
        try:
            subprocess.check_output(command, stderr=subprocess.STDOUT)
            # print(f"{host} is alive ")
            networkPing = 1
            return networkPing
        except subprocess.CalledProcessError:
            # print(f"{host} is not reachable")
            networkPing = 0
            return networkPing

    oldCommands = "oldCommands"
    # global loop_1
    loop_1 = 1
    while loop_1 == 1:
        if ping_host() == 1:
            # Ping Successful

            # Getting commands from the web////////////////////////////////////////////////////////////////////////////


            # commands runner////////////////////////////////////////////////////////////////////////////////////////

        else:
            print("Check your internet connection")

    time.sleep(0.5)

# Create threads
thread1 = threading.Thread(target=thredingGame)
thread2 = threading.Thread(target=thredingTrojen)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Done")
