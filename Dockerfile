FROM centos:latest

MAINTAINER RAHUL SIL <rahul.official.150@gmail.com>

RUN dnf install python3 ncurses net-tools -y && \
    pip3 install numpy pandas joblib scikit-learn

WORKDIR /root/ML

COPY * /root/ML/

RUN python3 salaryLR.py
 
CMD ["python3", "salary_predictor.py" ]
