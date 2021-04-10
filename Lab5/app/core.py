from flask import Flask, render_template
proyecto = Flask(_name_)

@proyecto.route('/')
def hola_mundo():
  return render_template('index.html')
