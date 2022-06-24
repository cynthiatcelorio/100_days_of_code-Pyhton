pulpi = input("Vas andando por la playa y tropiezas con algo. Le das una patada (P) o lo recoges (R)? ")
if pulpi == 'R':
    print('''
        ******************************************************
                        _,--._
                      ,'      `.
              |\     / ,-.  ,-. \     /|
              )o),/ ( ( o )( o ) ) \.(o(
             /o/// /|  `-'  `-'  |\  \o
            / / |\ \(   .    ,   )/ /| \ 
            | | \o`-/    `\/'    \-'o/ | |
            \ \  `,'              `.'  / /
         \.  \ `-'  ,'|   /\   |`.  `-' /  ,/
          \`. `.__,' /   /  \   \ `.__,' ,'/
           \o\     ,'  ,'    `.  `.     /o/
            \o`---'  ,'        `.  `---'o/
             `.____,'  -shimrod  `.____,'
        ********************************************************
       
    ''')
    print("\nHola, soy el pulpi Pulpi, muchas gracias por recogerme y no darme una patada como han hecho otros.")
    print("Te voy a recompensar con esta alga mágica, cómetela cuando estés en peligro.")
    print("\nSigues caminando, con una sonrisa en la cara por haber rescatado al pulpi Pulpi, pero de repente se cruza en tu camino un murciélago")
    print('''
            *****************************************************
                            
            _________________               _________________
            ~-.              \  |\___/|  /              .-~
                ~-.           \ / o o \ /           .-~
                   >           \\  W  //           <
                  /             /~---~\             \
                 /_            |       |            _\
                    ~-.        |       |        .-~
                       ;        \     /        i
                      /___      /\   /\      ___\
                           ~-. /  \_/  \ .-~
                              V         V
          *******************************************************  
            ''')
    murci = input("El murciélago viene a estamparse a tu cara y a atacarte, los esquivas (Y) o no lo esquivas (N)? ")
    if murci == 'Y':
        print("\nConsigues esquivar al murciélago, sigues con tu paseo por la playa.")
        print("\nTe vas a dar un chapuzón y ves a una mujer acercarse a ti por debajo del agua")
        print("\nSube a la superficie y ves que es una mujer hermosa")
        sirena = input("La mujer se acerca a ti, y ves que va a besarte. La besas (B) o la rechazas (R)? ")
        if sirena == 'B':
            print("Según te acercas a besarla ves que es una sirena, pero ya es demasiado tarde, ya te ha atrapado")
            print('''
                ***************************************************************************
                
                                __
               _o8o_o888888oo     _
                 o88888888 ,|    /#\
        \`.    /| `o88'88o _/    \_/
         \ `-.' |      __) \__   _Y_
          `-. .-'     /       \ /[_/
            | \      / (_(_ /\ y /
            |  \     \ /.  (  \_/
            |   \     V\____\
            \    `-._/      |
             \     _/      /
              \           /
               `-..___..-'

''')
            print("Te va arrastrando poco a poco al fondo del mar, notas como se te llenan los pulmones de agua. Has muerto.")
        else:
            print("\nTe dan miedo las mujeres, te vas nadando hacia la arena huyendo de la mujer. De la prisa que llevas al salir a la arena te tropiezas y te abres la cabeza con una piedra. Has muerto.")
    else:
        print("\nEl murciñelago te pega un bocao en la carótida, te desangras...")
        alga = input("Tienes el alga que te regaló el pulpi Pulpi, decides comértela (Y/N)? ")
        if alga == 'Y':
            print("\nEl alga sabe a mierda, la escupes y empiezas a sentir algo raro en tu cuerpo. Te estás mareando. De repente empiezas a sentir cómos se te hincha todo el cuerpo. No sabes qué te está pasando")
            print("\nVas corriendo al agua del mar para verte reflejado y ver qué te está pasando")
            print(''' Te miras y ves que ahora eres un dinosaurio, el pulpi Pulpi te ha engañado
            ***************************************************************************************     _
       .~q`,
      {__,  \
          \' \
           \  \
            \  \
             \  `._            __.__
              \    ~-._  _.==~~     ~~--.._
               \        '                  ~-.
                \      _-   -_                `.
                 \    /       }        .-    .  \
                  `. |      /  }      (       ;  \
                    `|     /  /       (       :   '\
                     \    |  /        |      /       \
                      |     /`-.______.\     |~-.      \
                      |   |/           (     |   `.      \_
                      |   ||            ~\   \      '._    `-.._____..----..___
                      |   |/             _\   \         ~-.__________.-~~~~~~~~~''
                     .o'___/            .o______}
            

            ***************************************************************************************
            ''')
            print("Miras al cielo y ves cómo a lo lejos se ve un meteorito acercarse a la Tierra. Miras atrás con temor buscando la mirada del pulpi Pulpi y puedes ver cómo te sonríe con una sonrisa diabólica. Se hace todo negro y mueres.")
else: 
    print("Acabas de matar al pulpi Pulpi, has perdido, suicídate, monstruo")