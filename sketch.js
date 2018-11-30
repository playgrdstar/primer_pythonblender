var currentPos = [];
var newPos = [];
var colorsPalette;
var numpoints = 80;

function setup() {

    c = createCanvas(600,600);
    c.parent('p5canvas');
    
    colorsPalette = [color(146, 167, 202,25),
            color(186, 196, 219,50),
            color(118, 135, 172,250),
            color(76, 41, 81,250),
            color(144, 62, 92,50),
            color(178, 93, 119,250),
            color(215, 118, 136,250),
            color(246, 156, 164,250),];
    background(colorsPalette[0]);

    frameRate(30);

    for (var i=0;i<numpoints;i++){        
        currentPos.push({
          x: random(width),
          y: random(height),
          c: colorsPalette[6]
        })    
    }
    for (var i=0;i<numpoints;i++){        
        newPos.push({
          x: random(width)+random(),
          y: random(height)+random(),
          c: colorsPalette[6]
        })    
    }

}

function draw() {
    
    background(colorsPalette[0]);

    if (frameCount%300==0){
        for (var i=0;i<numpoints;i++){      
            newPos[i].x = random(width)+random();
            newPos[i].y = random(height)+random();
        }

    }


    for (var i=0;i<numpoints;i++){
        TweenLite.to(currentPos[i], 10, newPos[i]);
        noStroke();
        fill(currentPos[i].c);
        ellipse(currentPos[i].x,currentPos[i].y,3,3);
        noStroke();
        fill(255,150);
        ellipse(currentPos[i].x+2,currentPos[i].y,1,1); 
        ellipse(currentPos[i].x-2,currentPos[i].y,1,1);   
    }

}

