from __main__ import app, render_template


@app.route('/iletisim')
def iletisim():
    data = dict()
    data['deneme']  = "deneme"
    data['header']  = render_template('klasik/header/header.html', data = data)
    data['menu']    = render_template('klasik/menu/menu.html', data = data)
    data['content'] = render_template('klasik/content/iletisim.html', data = data)
    data['footer']  = render_template('klasik/footer/footer.html', data = data)
    return render_template('klasik/index.html', data = data)