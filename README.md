# MagicF3M
Programa con el cual podrás utlizar ChatGPT en una ventana remota mucho mas discreta. Programa senzillo con acabados basicos, dejo el codigo para experimentar.

Antes de nada necesitas un codigo API. Pudes conseguirlo visitando https://platform.openai.com/account/api-keys (Tendras que logearte para poder crear un codigo API)

Una vez hecho esto, edita la variable ( openai.api_key = 'TU CODIGO' ). Con esto ya podrias ejecutarlo en la terminal o transfromarlo a .exe, por ejemplo con pyinstaller. 

1. Instalarse el pyinstaller: abres un terminal y tecleas *pip install pyinstaller*
  TERMINAL(cmd) = Windows + r *cmd* Enter:
    Ubicate en la carpeta donde tienes el scrpit y icono, utilizando cd *la ruta donde se encuentra el directorio*. Escribe el texto siguiente:
    *pyinstaller --windowed --onefile --icono=rocket.ico magicF3M.py*
2. Con esto ya tendras tu archivo .exe (Esta en la carpeta *dict*) Puedes extraerlo y borrar toda la carpeta anterior ya que no seran necearias. 

3. Prueba el programa

Y ya esta, tan solo tendras que poner tus preguntas en la text box.
