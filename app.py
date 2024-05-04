from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("calculator.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    # Inicializando variáveis
    resultado = None
    erro = None
    num1 = None
    num2 = None
    operacao = None

    try:
        # Limpando e convertendo os valores de entrada
        num1_str = request.form["num1"].replace(",", ".").strip()
        num2_str = request.form["num2"].replace(",", ".").strip()

        # Convertendo para float
        num1 = float(num1_str)
        num2 = float(num2_str)

        operacao = request.form["operacao"]

        # Realizando a operação selecionada
        if operacao == "soma":
            resultado = num1 + num2
        elif operacao == "subtracao":
            resultado = num1 - num2
        elif operacao == "multiplicacao":
            resultado = num1 * num2
        elif operacao == "divisao":
            if num2 != 0:
                resultado = num1 / num2
            else:
                erro = "Erro: Não é possível dividir por zero."

    except ValueError:
        erro = "Erro: Valores de entrada inválidos. Certifique-se de inserir números válidos."

    # Renderizando a página com o resultado ou erro
    return render_template(
        "calculator.html",
        resultado=resultado,
        num1=num1,
        num2=num2,
        operacao=operacao,
        erro=erro,
    )


if __name__ == "__main__":
    app.run()
