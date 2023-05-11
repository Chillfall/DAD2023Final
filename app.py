from flask import Flask, request, render_template
import random
import requests

app = Flask(__name__)

def status():
  n = 1
  stats = []
  while n < 8:
    roll = [
      random.randint(1, 6),
      random.randint(1, 6),
      random.randint(1, 6),
      random.randint(1, 6)
    ]
    roll.sort()
    roll.pop(0)
    stat = sum(roll)
    stats.append(stat)
    n += 1
  stats.sort()
  stats.pop(0)
  random.shuffle(stats)

  return stats

s = status()
str = (s[0]-10)/2
dex = (s[1]-10)/2
con = (s[2]-10)/2
int = (s[3]-10)/2
cha = (s[4]-10)/2
wis = (s[5]-10)/2



@app.route('/pet', methods = ['POST', 'GET'])
def welcome():
    global pet
    if request.method == 'POST':
        selection1 = request.form.get('selection1')
        if selection1 == '1':
            pet = 'dog'
            dogs_url = f'https://dog.ceo/api/breeds/image/random'
            response = requests.get(dogs_url)
            dogs_data = response.json()
            url = dogs_data['message']
        else: 
            pet = 'cat'
            cat = 'https://api.thecatapi.com/v1/images/search?'
            response = requests.get(cat)
            cat_data = response.json()
            url = cat_data[0]['url']
            
        return render_template('1.html', pet = pet, url = url)
    return render_template('0pet.html')



@app.route('/')
def Stats():
    return render_template('0.html', stats = s)

@app.route('/1first', methods = ['POST', 'GET'])
def first():
    des = ''
    if request.method == 'POST':
        selection1 = request.form.get('selection1')

        if selection1 == '1':
            if random.randint(1, 20) + str > 14:
                p1 = '2opendoor'
                des = 'You slammed the door open!'
            else: 
                p1 = '1fail'
                            
        elif selection1 == '2':
            if random.randint(1, 20) + dex > 12:
                p1 = '2opendoor'
                des = 'You picked the lock successfully'
            else: 
                p1 = '1fail'
        else:
            p1 = "2others"
        return render_template(f'{p1}.html', des = des)
    return render_template('1first.html', str = str, dex = dex)


@app.route('/2others', methods = ['POST', 'GET'])
def others():
    des = ''
    if request.method == 'POST':
        selection2 = request.form.get('selection2')

        if selection2 == '1':
            if random.randint(1, 20) + str > 20:
                p2 = '2opendoor'
                des = 'They are no match for you! You kicked their ass and they apologized. They also helped you to slam the door together. Under such strength, the door had to open. (It was actually broken instead of open, but same thing.)'
            else: 
                p2 = 'badending1'
                            
        elif selection2 == '2':
            if random.randint(1, 20) + cha > 15:
                p2 = '2opendoor'
                des = 'You successfully convinced them that their projects are better than yours, which is not true. However, they are very pleased with this idea and they stopped robbing your homework. They even helped you to slam the door together. Under such strength, the door had to open. (It was actually broken instead of open, but same thing.)'
            else: 
                p2 = 'badending2'

        return render_template(f'{p2}.html', des = des)
    return render_template('2others2.html', str = str, dex = dex)


@app.route('/3knight', methods = ['POST', 'GET'])
def knight():
    des = ''
    if request.method == 'POST':
        selection = request.form.get('selection')

        if selection == '1':
            p1 = 'badending3'
            des = 'She realized what you were trying to do and quickly reacted to it.'

                            
        elif selection == '2':
            if random.randint(1, 20) + cha > 20:
                p1 = '3moved'
                
            else: 
                p1 = 'badending3'
                des = 'You clearly cannot convince her that you are sincere. She thought that you are some random suspicious person hitting on her.'
        else:
            if random.randint(1, 20) + cha > 10:
                p1 = "3moved"
            else: 
                p1 = 'badending3'
                des = 'You clearly cannot convince her that you are sincere. She thought that you are some random suspicious person hitting on her.'
        if pet == 'cat':
            key = '4cat'
        else:
            key = '4hidden'
        return render_template(f'{p1}.html', des = des, key = key)
    return render_template('3knight.html', cha = cha)



@app.route('/4hidden', methods = ['POST', 'GET'])
def hidden():

    if request.method == 'POST':
        selection = request.form.get('selection')

        if selection == '1':
            if random.randint(1, 20) + wis > 20:
                p1 = '4found'
                
            else: 
                if random.randint(1, 20) + con > 12:
                    p1 = '4healthy'
                else:
                    p1 = 'badending4'
                                  
        elif selection == '2':
            if random.randint(1, 20) + int > 14:
                p1 = '4found'
                
            else: 
                p1 = 'badending4'
                
        if pet == 'dog':
            key = '5dog'
        else:
            key = '5math'
        return render_template(f'{p1}.html', key = key)
    return render_template('4hidden.html', wis = wis, int = int, con = con)


@app.route('/4cat')
def catt():
    return render_template('4cat.html')

@app.route('/5math', methods = ['POST', 'GET'])
def math():
    des = ''
    if request.method == 'POST':
        selection = request.form.get('selection')

        if selection == '1':
            
            p1 = '5toproblem'
                                  
        elif selection == '2':
            if random.randint(1, 20) + dex > 16:
                p1 = '5done'
                des = "You handed him the piece of paper with some bullshit on it. He starts to read it. You quickly sneaked past him, impressively making no noise at all! After a second of sneaking past the room, you heard him yelling angrily, but that's none of your business anymore."

                
            else: 
                p1 = 'badending5'
                des = "You handed him the piece of paper with some bullshit on it. He starts to read it. You quickly tried to sneak past him, but he heard your footsteps. "

        else:
            if random.randint(1, 20) + con > 10:
                p1 = '5done'
                des = "You ignored the math problem and waved your punches right at him! He's a shadow in a fire, so you got burned a little. However, it seems that a few punches made his image flicker. Now he doesn't have the power to block you anymore!!"

                
            else: 
                p1 = 'badending5'
                des = "You ignored the math problem and waved your punches right at him! He wasn't able to fight back or anything, since he's a shadow. But he IS in a flame, and you breathed some smoke and got burned. It's not a big deal, but it seems that you are really unhealthy, so you fainted. After you woke up..."

        return render_template(f'{p1}.html', des = des)
    return render_template('5math.html', dex = dex, con = con)

@app.route('/5toproblem')
def topr():
    return render_template('5toproblem.html')

@app.route('/5problem', methods = ['POST', 'GET'])
def problem():
    des = ''
    if request.method == 'POST':
        x1 = request.form['x1']
        x2 = request.form['x2']
        x3 = request.form['x3']
        if x1 == '19' and x2 == '-8' and x3 == '1':
            p1 = '5done'
            des = 'You are correct! The Math God is impressed. He happily sings a song for you as you walk into the next room.'
        else:
            p1 = 'badending5'
            des = 'It seems that your answers are wrong.'
        return render_template(f'{p1}.html', des = des)
    return render_template('5problem.html')


@app.route('/5dog')
def dogg():
    return render_template('5dog.html')

@app.route('/6empty', methods = ['POST', 'GET'])
def empty():
    des = ''
    if request.method == 'POST':
        selection = request.form.get('selection')

        if selection == '1':
            p1 = 'office_end'
            des = 'You walked straight into that door in front of you, which has an office sign.'
                                  
        elif selection == '2':
            if random.randint(1, 20) + wis > 12:
                if random.randint(1, 20) + int > 16:
                    p1 = 'treasure_end'
                else:
                    p1 = 'office_end'
                    des = 'As you investigate, more and more whispers begin to fill in your ears. Darkness climbs into your eyes, trying to take over your thoughts.And your brains. When you were about to get distracted by these silly thoughts, you saw the cute face of your {{pet}}. You quickly realized that these are just voices in your head. You cannot believe that you were thinking this nonsense!You calmed down and start investigating carefully. Unfortunately, you did not find anything. You shrugged and went into the office in front of you.'
            else: 
                p1 = 'badending6'
                

        return render_template(f'{p1}.html', pet = pet, des = des)
    return render_template('6empty.html', wis = wis, int = int)


    
if __name__ == '__main__':
    app.run(debug=True)