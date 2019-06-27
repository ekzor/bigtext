#!/usr/bin/env python

class BigText(object):

  big_chars = {
    '6x5' : {
      'A' : ['CCCCCC','CC  CC','CCCCCC','CC  CC','CC  CC'],
      'B' : ['CCCCC ','CC  CC','CCCCC ','CC  CC','CCCCCC'],
      'C' : ['CCCCCC','CC    ','CC    ','CC    ','CCCCCC'],
      'D' : ['CCCCC ','CC   C','CC   C','CC   C','CCCCC '],
      'E' : ['CCCCCC','CC    ','CCCC  ','CC    ','CCCCCC'],
      'F' : ['CCCCCC','CC    ','CCCC  ','CC    ','CC    '],
      'G' : ['CCCCCC','CC    ','CC  CC','CC   C','CCCCCC'],
      'H' : ['CC  CC','CC  CC','CCCCCC','CC  CC','CC  CC'],
      'I' : ['CCCCCC','  CC  ','  CC  ','  CC  ','CCCCCC'],
      'J' : ['CCCCCC','   C  ','   C  ','C  C  ','CCCC  '],
      'K' : ['CC   C','CC  C ','CCCC  ','CC  C ','CC   C'],
      'L' : ['CC    ','CC    ','CC    ','CC    ','CCCCCC'],
      'M' : ['C    C','CC  CC','C CC C','C    C','C    C'],
      'N' : ['CC   C','CCC  C','CC C C','CC  CC','CC   C'],
      'O' : ['CCCCCC','CC  CC','CC  CC','CC  CC','CCCCCC'],
      'P' : ['CCCCCC','CC  CC','CCCCCC','CC    ','CC    '],
      'Q' : [' CCCC ','C    C','C    C','C  C C',' CCCCC'],
      'R' : ['CCCCC ','CC   C','CCCCC ','CC  C ','CC   C'],
      'S' : [' CCCCC','CC    ','  CCC ','    CC','CCCCC '],
      'T' : ['CCCCCC','  CC  ','  CC  ','  CC  ','  CC  '],
      'U' : ['CC  CC','CC  CC','CC  CC','CC  CC','CCCCCC'],
      'V' : ['C    C','C    C','C    C',' C  C ','  CC  '],
      'W' : ['C    C','C    C','C CC C','CC  CC','C    C'],
      'X' : ['C    C',' C  C ','  CC  ',' C  C ','C    C'],
      'Y' : ['C    C','CC  CC','  CC  ','  CC  ','  CC  '],
      'Z' : ['CCCCCC','   CC ','  CC  ',' CC   ','CCCCCC'],
      '0' : ['CCCCCC','CC   C','C C  C','C   CC','CCCCCC'],
      '1' : ['CCCC  ','  CC  ','  CC  ','  CC  ','CCCCCC'],
      '2' : ['CCCCC ','    CC','  CCC ','CC    ','CCCCCC'],
      '3' : ['CCCCCC','    C ','   C  ','    CC','CCCCCC'],
      '4' : ['CC  CC','CC  CC','CCCCCC','    CC','    CC'],
      '5' : ['CCCCCC','CC    ','CCCCCC','    CC','CCCCCC'],
      '6' : ['CCCCCC','CC    ','CCCCCC','CC  CC','CCCCCC'],
      '7' : ['CCCCCC','    CC','  CC  ','  CC  ','  CC  '],
      '8' : ['CCCCCC','CC  CC','CCCCCC','CC  CC','CCCCCC'],
      '9' : ['CCCCCC','CC  CC','CCCCCC','    CC','CCCCCC'],
      '+' : ['      ','  CC  ','CCCCCC','  CC  ','      '],
      '-' : ['      ','      ','CCCCCC','      ','      ']

    }
  }

  def __init__(self,phrase,pieces,spacer_chars="  ",spacer_words="   ",padding=" ",before="",reset_each_line=True,charwidth=6,lineheight=5):
    self.phrase = phrase.upper()  #convert phrase to uppercase, since upper-case fonts are only supported at this time
    self.pieces = pieces
    self.width = charwidth
    self.height = lineheight
    self.size = str(charwidth)+'x'+str(lineheight)
    self.padding = padding
    self.before = before
    self.spacer_chars = spacer_chars
    self.spacer_words = spacer_words
    
    self.shape = self.make_shape()
    self.output_list = self.make_output(reset_each_line)
    
  
  def get_output(self):
    return '\n'.join(self.output_list)

  def make_shape(self):
    #initialize an empty list
    shape = ['' for _ in range(self.height)]

    #loop through the characters in the phrase
    for phrase_index,char in enumerate(self.phrase):
      #no space before the first letter
      if phrase_index > 0:
        between_chars = True
      else:
        between_chars = False
      #if we're at a space in the phrase, insert the word spacer
      if self.phrase[phrase_index] == " ":
        for line in range(self.height):
          shape[line] += self.spacer_words
      
      #skip the character if it's not part of our characterset
      elif char not in self.big_chars[self.size]:
        continue
      
      #otherwise we're looking at a bigtext character
      else:
        for line in range(self.height):
          shape[line] += between_chars*self.spacer_chars + self.big_chars[self.size][char][line] 

    return shape
      
      
  def make_output(self,reset_each_line=True):
    #use shape to generate output
    output = [self.before for _ in range(self.height)]
    #track position in the piece string
    piece_index = 0
    #loop through all lines in the shape, as defined by self.height.
    for line in range(self.height):
      #loop through the characters in the line
      for char in self.shape[line]:
        #if it's a character to be filled, throw in the next character from the pieces string
        if char == "C":
          output[line] += self.pieces[piece_index%len(self.pieces)]
          piece_index += 1
        #if it's a space, throw in our padding character
        elif char == " ":
          output[line] += self.padding
      
      #reset the piece_index if we're meant to reset for each line
      piece_index *= not(reset_each_line)
      
    return output
          

if __name__ == '__main__':
  import argparse as ap
  argparser = ap.ArgumentParser()
  argparser.add_argument("big", help="characters to make big")
  argparser.add_argument("pieces", help="characters to fill in the big text shape")
  argparser.add_argument("-c", "--charsep", help="separator between big characters",default="  ")
  argparser.add_argument("-w", "--wordsep", help="separator between big words",default="   ")
  argparser.add_argument("-p", "--padding", help="padding character for blank spots in big characters", default=" ")
  argparser.add_argument("-b", "--before", help="prepend each line with these characters. useful for forum formatting", default="")
  argparser.add_argument("-r", "--nolinereset", help="start each line at the beginning of the pieces string",action='store_false')
  args = argparser.parse_args()
    
  bt = BigText(args.big,args.pieces,args.charsep,args.wordsep,args.padding,args.before,args.nolinereset)
  print '\n' + bt.get_output() + '\n'
