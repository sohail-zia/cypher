
def encoder(alpha):
  user_input = input("Enter your text: ").lower()
  shift = int(input("Enter your shift: "))
  shift = shift%26
  encoder = ''
  for i in user_input:
    index = alpha.index(i) + shift
    encoder = encoder + alpha[index]
  return encoder

#decoder

def decoder(alpha):
  user_input = input("Enter your text: ").lower()
  shift = int(input("Enter your shift: "))
  shift = shift%26

  decoder=''
  for i in user_input:
    index = alpha.index(i) - shift
    decoder = decoder + alpha[index]
  return decoder
