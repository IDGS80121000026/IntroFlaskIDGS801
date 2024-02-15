from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,TelField,IntegerField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    nombre= StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa nombre valido')
    ])
    apaterno= StringField('apaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa apellido valido')
    ])
    amaterno= StringField('amaterno',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa apellido valido')
    ])
    email= EmailField('email',[
        validators.Email(message='Ingresa un correo valido')
    ])
    edad= IntegerField('edad',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10, message='Ingresa una edad valida')
    ])