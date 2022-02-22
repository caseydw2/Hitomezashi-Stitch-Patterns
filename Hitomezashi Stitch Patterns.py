# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:38:48 2022

@author: Casey


Input phrase1 and phrase2. phrase1 is responsible for the vertical lines. phrase 2 the horizontal. Convert the phrases to upercase and no space strings. 
Cycle through the phrase. Draw lines on even spaces for vowels. Odd spaces for consenants.

"""
from PIL import Image, ImageDraw

factor = 50


def squish_upper(phrase):
    """
    

    Parameters
    ----------
    phrase : string
        

    Returns
    -------
    phrase : string
        The previous phrase with no spaces,punctuation, and all upper case.
        

    """
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in phrase:
        if i in punc:
            phrase = phrase.replace(i,"")
    phrase = phrase.upper().replace(" ","")
    return phrase



def isvowel(letter):
    '''
    

    Parameters
    ----------
    letter : string
        

    Returns
    -------
    bool
        returns True if the letter is A,E,I,O,U, or Y. False otherwise.

    '''
    if letter in "AEIOUY":
        return True
    else:
        return False




def stitch_line(im, num, coor, factor, horizontal= True, on= True ):
    '''
    

    Parameters
    ----------
    im : image
        The image to stitch a line on.
    num : int
        number of stitches to make.
    coor : int
        fixed coordinate.
    factor : int
        number of pixels per letter.
    horizontal : bool, optional
        True if stiches go horizontaly. False if vertically. The default is True.
    on : bool, optional
        Starts stitching in initial position. The default is True.

    Returns
    -------
    None.

    '''
    draw = ImageDraw.Draw(im)
    for k in range(num):
        a, b, c, d = coor * factor , 2*k*factor, (2*k + 1)*factor, 2*(k+1)*factor
        if on:
            if horizontal:
                draw.line([(b,a),(c,a)],width=2)
            else:
                draw.line([(a,b),(a,c)],width=2)
        else:
            if horizontal:
                draw.line([(c,a),(d,a)],width=2)
            else:
                draw.line([(a,c),(a,d)],width=2)
    
        
def stitch_pattern(phrase1,phrase2):
    '''
    

    Parameters
    ----------
    phrase1 : TYPE
        phrase for horizontal stitching.
    phrase2 : TYPE
        phrase for vertical stitching.

    Returns
    -------
    picture of the stitch pattern with the two phrases.

    '''
    phrase1,phrase2 = squish_upper(phrase1),squish_upper(phrase2)
    W,H = factor*len(phrase2) ,factor*len(phrase1)
    im= Image.new("RGB",(W,H),(0,0,0))
    for i,letter in enumerate(phrase1):
        if len(phrase2) % 2 == 0:
            num = int(len(phrase2) / 2)
        else:
            if isvowel(letter):
                num = int((len(phrase2)+1)/2)
            else:
                num = int((len(phrase2)-1)/2)
        stitch_line(im,num,i,factor,on = isvowel(letter))
    for i,letter in enumerate(phrase2):
        if len(phrase1) % 2 == 0:
            num = int(len(phrase1) / 2)
        else:
            if isvowel(letter):
                num = int((len(phrase1)+1)/2)
            else:
                num = int((len(phrase1)+1)/2)
        stitch_line(im,num,i,factor,horizontal = False, on = isvowel(letter))    
    im.show()


