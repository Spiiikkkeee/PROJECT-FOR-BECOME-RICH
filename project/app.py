from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
appsecret_key = "your_seceret_key"


#sample date

students = {
    "1001": {"name": "Akansha", "Class": "10", "fees_due": 5000, "status": "Unpaid"},
    "1002": {"name": "Rahul", "Class": "12", "fees_dues": 7000, "status": "Unpaid"},

}

@app.route('/')
def index():
    return render_template('index.html', students=students)


@app.route('/pay/<student_id>', methods=['GET', 'POST'])
def pay(student_id):
    student = student.get(student_id)
    if not student:
        flash("Student not found!", "error")
        return redirect(url_for('index'))


    if request.method == 'POST':
        amount = int(request.form['amount'])
        if amount >= student['fees_due']:
            student['status'] = 'Paid'
            flash('Payment successfull', "success")

        else:
            student['fees_dues'] -= amount
            flash("Partial payment accepted!", "info")

        return redirect(url_for('index'))


    return render_template('pay.html', student=student)


if __name__ == '__main__':
    app.run(debug=True)