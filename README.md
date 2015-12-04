* Change Spender

TODO: explain project

** Installation instructions

Assumes npm and virtualenvwrapper are installed.
TODO: elaborate on how to get those

TODO: be more detailed about what these instructions are doing and why

    git clone https://github.com/kamni/change-spender.git
    cd change-spender.git
    mkvirtualenv --no-site-packages change-spender
    pip install -r requirements.txt
    npm install
    npm install --only=dev  # not necessary if you're not doing development. May need to use --dev for older versions of node
    mkdir static
    python manage.py collectstatic
    ./node_modules/.bin/webpack --config webpack.config.js  #TODO: is there a pipeline to incorporate this into collectstatic?
    python manage.py migrate
    python manage.py runserver