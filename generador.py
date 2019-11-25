
# Aqui se importan las librerias para el manejo de imagenes
from PIL import Image, ImageFont, ImageDraw
import imghdr
# Aqui se importan las librerias para el manejo de emails
import smtplib
from email.message import EmailMessage
# Aqui se importan las librerias para el manejo de bases de datos en csv
import pandas

# ------------------------------Se obtiene el documento csv y se lo lee---------------------------------

print("leyendo base de datos...")

base_de_datos = pandas.read_csv('Base.csv')
contadorDeDiplomas = 0
cuerpo_mail = """
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <meta charset="utf-8"> <!-- utf-8 works for most cases -->
    <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
    <meta name="x-apple-disable-message-reformatting"> <!-- Disable auto-scale in iOS 10 Mail entirely -->
    <title></title> <!-- The title tag shows in email notifications, like Android 4.4. -->


    <link href="https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i" rel="stylesheet">

    <!-- CSS Reset : BEGIN -->
    <style>
        html,
        body {
            margin: 0 auto !important;
            padding: 0 !important;
            height: 100% !important;
            width: 100% !important;
            background: #f1f1f1;
        }

        /* What it does: Stops email clients resizing small text. */
        * {
            -ms-text-size-adjust: 100%;
            -webkit-text-size-adjust: 100%;
        }

        /* What it does: Centers email on Android 4.4 */
        div[style*="margin: 16px 0"] {
            margin: 0 !important;
        }

        /* What it does: Stops Outlook from adding extra spacing to tables. */
        table,
        td {
            mso-table-lspace: 0pt !important;
            mso-table-rspace: 0pt !important;
        }

        /* What it does: Fixes webkit padding issue. */
        table {
            border-spacing: 0 !important;
            border-collapse: collapse !important;
            table-layout: fixed !important;
            margin: 0 auto !important;
        }

        /* What it does: Uses a better rendering method when resizing images in IE. */
        img {
            -ms-interpolation-mode: bicubic;
        }

        /* What it does: Prevents Windows 10 Mail from underlining links despite inline CSS. Styles for underlined links should be inline. */
        a {
            text-decoration: none;
        }

        /* What it does: A work-around for email clients meddling in triggered links. */
        *[x-apple-data-detectors],
        /* iOS */
        .unstyle-auto-detected-links *,
        .aBn {
            border-bottom: 0 !important;
            cursor: default !important;
            color: inherit !important;
            text-decoration: none !important;
            font-size: inherit !important;
            font-family: inherit !important;
            font-weight: inherit !important;
            line-height: inherit !important;
        }

        /* What it does: Prevents Gmail from displaying a download button on large, non-linked images. */
        .a6S {
            display: none !important;
            opacity: 0.01 !important;
        }

        /* What it does: Prevents Gmail from changing the text color in conversation threads. */
        .im {
            color: inherit !important;
        }

        /* If the above doesn't work, add a .g-img class to any image in question. */
        img.g-img+div {
            display: none !important;
        }

        /* What it does: Removes right gutter in Gmail iOS app: https://github.com/TedGoas/Cerberus/issues/89  */
        /* Create one of these media queries for each additional viewport size you'd like to fix */
        /* iPhone 4, 4S, 5, 5S, 5C, and 5SE */
        @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {
            u~div .email-container {
                min-width: 320px !important;
            }
        }

        /* iPhone 6, 6S, 7, 8, and X */
        @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {
            u~div .email-container {
                min-width: 375px !important;
            }
        }

        /* iPhone 6+, 7+, and 8+ */
        @media only screen and (min-device-width: 414px) {
            u~div .email-container {
                min-width: 414px !important;
            }
        }
    </style>

    <!-- CSS Reset : END -->

    <!-- Progressive Enhancements : BEGIN -->
    <style>
        .primary {
            background: #f3a333;
        }

        .bg_white {
            background: #ffffff;
        }

        .bg_light {
            background: #fafafa;
        }

        .bg_black {
            background: #000000;
        }

        .bg_dark {
            background: rgba(0, 0, 0, .8);
        }

        .email-section {
            padding: 2.5em;
        }

        /*BUTTON*/
        .btn {
            padding: 10px 15px;
        }

        .btn.btn-primary {
            border-radius: 30px;
            background: #810c33;
            color: #ffffff;
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
            color: #000000;
            margin-top: 0;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            font-weight: 400;
            font-size: 15px;
            line-height: 1.8;
            color: rgba(0, 0, 0, .4);
        }

        a {
            color: #f3a333;
        }

        table {}

        /*LOGO*/
        .logo h1 {
            margin: 0;
        }

        .logo h1 a {
            color: #000;
            font-size: 20px;
            font-weight: 700;
            text-transform: uppercase;
            font-family: 'Montserrat', sans-serif;
        }

        /*HERO*/
        .hero {
            position: relative;
        }

        .hero img {}

        .hero .text {
            color: rgba(255, 255, 255, .8);
        }

        .hero .text h2 {
            color: #ffffff;
            font-size: 30px;
            margin-bottom: 0;
        }

        /*HEADING SECTION*/
        .heading-section {}

        .heading-section h2 {
            color: #000000;
            font-size: 28px;
            margin-top: 0;
            line-height: 1.4;
        }

        .heading-section .subheading {
            margin-bottom: 20px !important;
            display: inline-block;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: rgba(0, 0, 0, .4);
            position: relative;
        }

        .heading-section .subheading::after {
            position: absolute;
            left: 0;
            right: 0;
            bottom: -10px;
            content: '';
            width: 100%;
            height: 2px;
            background: #f3a333;
            margin: 0 auto;
        }

        .heading-section-white {
            color: rgba(255, 255, 255, .8);
        }

        .heading-section-white h2 {
            font-size: 28px;
            font-family:
                line-height: 1;
            padding-bottom: 0;
        }

        .heading-section-white h2 {
            color: #ffffff;
        }

        .heading-section-white .subheading {
            margin-bottom: 0;
            display: inline-block;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: rgba(255, 255, 255, .4);
        }

        .icon {
            text-align: center;
        }

        .icon img {}

        /*SERVICES*/
        .text-services {
            padding: 10px 10px 0;
            text-align: center;
        }

        .text-services h3 {
            font-size: 20px;
        }

        /*BLOG*/
        .text-services .meta {
            text-transform: uppercase;
            font-size: 14px;
        }

        /*TESTIMONY*/
        .text-testimony .name {
            margin: 0;
        }

        .text-testimony .position {
            color: rgba(0, 0, 0, .3);
        }

        /*VIDEO*/
        .img {
            width: 100%;
            height: auto;
            position: relative;
        }

        .img .icon {
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            bottom: 0;
            margin-top: -25px;
        }

        .img .icon a {
            display: block;
            width: 60px;
            position: absolute;
            top: 0;
            left: 50%;
            margin-left: -25px;
        }

        /*COUNTER*/
        .counter-text {
            text-align: center;
        }

        .counter-text .num {
            display: block;
            color: #ffffff;
            font-size: 34px;
            font-weight: 700;
        }

        .counter-text .name {
            display: block;
            color: rgba(255, 255, 255, .9);
            font-size: 13px;
        }

        /*FOOTER*/
        .footer {
            color: rgba(255, 255, 255, .5);
        }

        .footer .heading {
            color: #ffffff;
            font-size: 20px;
        }

        .footer ul {
            margin: 0;
            padding: 0;
        }

        .footer ul li {
            list-style: none;
            margin-bottom: 10px;
        }

        .footer ul li a {
            color: rgba(255, 255, 255, 1);
        }

        @media screen and (max-width: 500px) {
            .icon {
                text-align: left;
            }

            .text-services {
                padding-left: 0;
                padding-right: 20px;
                text-align: left;
            }
        }
    </style>


</head>

<body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #222222;">
    <center style="width: 100%; background-color: #f1f1f1;">
        <div
            style="display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
            &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
        </div>
        <div style="max-width: 600px; margin: 0 auto;" class="email-container">
            <!-- BEGIN BODY -->
            <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%"
                style="margin: auto;">
                <tr>
                    <td class="bg_white logo" style="padding: 1em 2.5em; text-align: center">
                        <h1><a href="http://uees.edu.ec/">Universidad Espíritu Santo</a></h1>
                    </td>
                </tr><!-- end tr -->
                <tr>
                    <td valign="middle" class="hero"
                        style="background-image: url(slider_3.jpg); background-size: cover; height: 400px;">
                        <table>
                            <tr>
                                <td>
                                    <div class="text" style="padding: 0 3em; text-align: center;">
                                        <h2>Concurso Beca Completa</h2>
                                        <br>
                                        <p><a href="http://uees.edu.ec/" class="btn btn-primary">Conoce más sobre la
                                                UEES</a></p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr><!-- end tr -->
                <tr>
                    <td class="bg_white">
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                            <tr>
                                <td class="bg_dark email-section" style="text-align:justify;">
                                    <div class="heading-section heading-section-white">
                                        <p>
                                            Gracias por participar en nuestro concurso, <b>"Gánate una beca
                                                Completa"</b>, a
                                            través del cual recibimos tu ensayo que fue revisado por nuestro Comité
                                            Académico el cual reconoce tu esfuerzo y dedicación.
                                        </p>
                                        <p>
                                            Por tal motivo estamos gustosos de conceder la entrega del diploma de
                                            participación del mismo.
                                        </p>

                                    </div>
                                    <br>
                                    <div class="heading-section heading-section-white" align="center">
                                        <h2>
                                            <b>Gracias por participar con nosotros</b>
                                        </h2>
                                    </div>


                                </td>
                            </tr><!-- end: tr -->

                        </table>

        </div>
    </center>
</body>

</html>
"""

for row in base_de_datos.head(1).itertuples():
    # Importante
    # Row[2] = correos
    # Row[3] = nombres
    # Row[4] = apellidos
    # Row[5] = titulo del ensayo
    # Row[6] = nombre del tutor
    # Row[7] = Documento enviado
    # Row[8] = posee tutor?

    print()
    print("---------------------------------------------------------")
    print(row)
    print("Generando diploma numero: " + str(contadorDeDiplomas))
    # ------------------------------------------------------------------------------------------------------
    # ------------------------------Se obtiene la imagen para procesarla con el nuevo texto-----------------

    if(isinstance(row[3], str) or isinstance(row[4], str)):

         # ------------------------------Pregunta si tiene tutor o no -------------------------------------------
        if(row[8] == "si"):

            cambioDeNombres = 0

            imgProfe = Image.open('diploma.jpg')
            # Selecciona el nombre del tutor
            Nombre_Tutor = ""+str(row[6])
            destinoTutor = "C:/Users/User/Desktop/Generador de pdfs/Diplomas/Tutores/diploma" + \
                str(contadorDeDiplomas)+".jpg"

            font = ImageFont.truetype("avenir.ttf", 160)
            w, h = font.getsize(Nombre_Tutor)

            draw = ImageDraw.Draw(imgProfe)
            x = (5100-w)/2
            y = (3000-h)/2
            draw.text((x, y), Nombre_Tutor, (84, 84, 84), font=font)

            imgProfe.copy()
            imgProfe.save(destinoTutor, 'JPEG', quality=80, optimize=True)
            print("Diploma de profesor generado!")
            print("Generando diploma de profesor...")

            # ------------------------------------------------------------------------------------------------------
            imgAlumno = Image.open('diploma.jpg')
            Nombre_Persona = ""+str(row[3])+" "+str(row[4])
            destinoAlumno = "C:/Users/User/Desktop/Generador de pdfs/Diplomas/Alumnos/diploma" + \
                str(contadorDeDiplomas)+".jpg"

            font = ImageFont.truetype("avenir.ttf", 160)
            w, h = font.getsize(Nombre_Persona)

            draw = ImageDraw.Draw(imgAlumno)
            x = (5100-w)/2
            y = (3000-h)/2
            draw.text((x, y), Nombre_Persona, (84, 84, 84), font=font)

            imgAlumno.copy()
            imgAlumno.save(destinoAlumno, 'JPEG', quality=80, optimize=True)
            print("Diploma de alumno generado!")

            # ------------------------------Se Crea el nuevo email con el que sera guardada la fotografia-----------

            print("Generando el correo electrónico...")
            EMAIL_ADDRES = "advillegas@uees.edu.ec"
            EMAIL_PASSWORD = "094504722a"

            contact = row[2]

            msg = EmailMessage()
            msg['subject'] = 'Test'
            msg['from'] = EMAIL_ADDRES
            msg['to'] = contact

            msg.set_content('Certificado de participación')
            msg.add_alternative(mail.html, subtype='html')

            diplomas = [destinoAlumno, destinoTutor]

            for diploma in diplomas:
                with open(diploma, 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    if(cambioDeNombres == 0):
                        file_name = "Diploma de Participación Alumno"
                    else:
                        file_name = "Diploma de Participación Tutor"
                    cambioDeNombres += 1

                msg.add_attachment(file_data, maintype='image',
                                   subtype=file_type, filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRES, EMAIL_PASSWORD)
                smtp.send_message(msg)

            # ------------------------------------------------------------------------------------------------------
            contadorDeDiplomas += 1
            print("Correo enviado correctamente!")
            print("---------------------------------------------------------")
            print("Siguiente...")

        else:

            imgAlumno = Image.open('diploma.jpg')
            Nombre_Persona = ""+str(row[3])+" "+str(row[4])
            destinoAlumno = "C:/Users/User/Desktop/Generador de pdfs/Diplomas/Alumnos/diploma" + \
                str(contadorDeDiplomas)+".jpg"

            font = ImageFont.truetype("avenir.ttf", 160)
            w, h = font.getsize(Nombre_Persona)

            draw = ImageDraw.Draw(imgAlumno)
            x = (5100-w)/2
            y = (3000-h)/2
            draw.text((x, y), Nombre_Persona, (84, 84, 84), font=font)

            imgAlumno.copy()
            imgAlumno.save(destinoAlumno, 'JPEG', quality=80, optimize=True)
            print("Diploma de alumno generado!")

            # ------------------------------------------------------------------------------------------------------

            # ------------------------------Se Crea el nuevo email con el que sera guardada la fotografia-----------

            print("Generando el correo electrónico...")
            EMAIL_ADDRES = "advillegas@uees.edu.ec"
            EMAIL_PASSWORD = "094504722a"

            contact = row[2]

            msg = EmailMessage()
            msg['subject'] = 'Diploma de participación - Beca completa UEES'
            msg['from'] = EMAIL_ADDRES
            msg['to'] = contact

            msg.set_content('Certificado de participación')
            msg.add_alternative(mail.html, subtype='html')

            with open(destinoAlumno, 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = "Diploma de Participación"

            msg.add_attachment(file_data, maintype='image',
                               subtype=file_type, filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRES, EMAIL_PASSWORD)
                smtp.send_message(msg)

            # ------------------------------------------------------------------------------------------------------
            contadorDeDiplomas += 1
            print("Correo enviado correctamente!")
            print("---------------------------------------------------------")
            print("Siguiente...")
    else:
        print("El diploma numero: " + str(contadorDeDiplomas) +
              " No cuenta con sus nombres escritos correctamente")
        contadorDeDiplomas += 1
