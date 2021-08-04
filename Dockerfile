FROM python:3.8
EXPOSE 8502
WORKDIR /API
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . /API
CMD streamlit run streamlit_pred.py