import turtle
import random

# Ana Ekran
game_board = turtle.Screen()
game_board.title("Catch The Turtle")
game_board.bgcolor("light blue")

score = 0

# Kaplumbağa
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(2, 2)
turtle_instance.penup()

# Skor Yazısı
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("black")
score_turtle.penup()
score_turtle.goto(0, 240)
score_turtle.write("Skor: 0", align="center", font=("Arial", 24, "normal"))

# Geri Sayım Yazısı
countdown_turtle = turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.color("black")
countdown_turtle.penup()
countdown_turtle.goto(0, 200)

click_allowed = True


# Skoru Yükseltme
def increase_score(x, y):
    global score, click_allowed
    if click_allowed:
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))
        click_allowed = False
        game_board.ontimer(reset_click, 1000)


# Tıklamayı Sıfırlama
def reset_click():
    global click_allowed
    click_allowed = True


# Skor Yükseltme
turtle_instance.onclick(increase_score)


# Işınlanma
def teleport_turtle():
    turtle_instance.hideturtle()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    turtle_instance.goto(x, y)
    turtle_instance.showturtle()
    game_board.ontimer(teleport_turtle, 500)


# Geri Sayım
def countdown_timer(count):
    countdown_turtle.clear()
    if count > 0:
        countdown_turtle.write(f"Kalan Süre: {count} saniye", align="center", font=("Arial", 24, "normal"))
        game_board.ontimer(lambda: countdown_timer(count - 1), 1000)
    else:
        countdown_turtle.clear()
        countdown_turtle.write("Süre Doldu!", align="center", font=("Arial", 24, "normal"))
        game_board.ontimer(stop_game, 2000)  # Oyunu 2 saniye sonra kapat


def stop_game():
    turtle.done()


countdown_timer(20)

teleport_turtle()

turtle.mainloop()