From python: 3.13
COPY . . 
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["main.py"]