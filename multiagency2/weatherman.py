import csv
import tomllib

import requests

from uagents import Agent, Model, Context


class WeatherRequest(Model):
    county: str
    state: str


class WeatherReport(Model):
    condition: bool  # good or bad


# agent1qv7h7t3fxqpkxvnzuy5yh4a8z4jd5tvlv7s7hnxyxxwgglrzn4cgxnwt970
weatherman = Agent(name = "weatherman", seed = "weatherman")


@weatherman.on_event("startup")
def init(ctx: Context):
    ctx.logger.info(f"Weatherman: {ctx.address}")

@weatherman.on_query(model = WeatherRequest, replies = {WeatherReport})
def on_request(ctx: Context, sender: str, msg: WeatherRequest):
    print("COUNTY:", msg.county, msg.state)
    zipcode = 0

    with open('uszips.csv') as csvfile:
        county_zips = csv.reader(csvfile, delimiter = ",")

        for row in county_zips:
            if msg.county == row[11] and msg.state == row[5]:
                print("ZIP:", row[0])
                zipcode = row[0]
                break

    with open("../secrets.toml", "rb") as f:
        data = tomllib.load(f)

    key = data["weather"]["KEY"]

    resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={key}").json()

    description = resp["weather"][0]["description"]
    temperature = resp["main"]["temp"]-273.15
    humidity = resp["main"]["humidity"]
    wind_speed = resp["wind"]["speed"]  # m/s

    if 5.0 <= temperature <= 30.0 and 10.0 <= humidity <= 90.0 and 0.0 <= wind_speed <= 2.0:
        ctx.send(sender, WeatherReport(condition = True))
    else:
        ctx.send(sender, WeatherReport(condition = False))


if __name__ == '__main__':
    weatherman.run()

    # zipcode = 92620
    # resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={key}").json()
    #
    # description = resp["weather"][0]["description"]
    # temperature = resp["main"]["temp"]-273.15
    # humidity = str(resp["main"]["humidity"])+"%"
    # wind_speed = str(resp["wind"]["speed"])+"m/s"
    # event_title = "Environmental Engineering Challenge"
    # print(f"The weather right now is {description} with {temperature}C degree, {humidity} humidity, and {wind_speed} wind speed. Is it a good time to go out for {event_title}? Give it out of a single rating between 0 (bad) and 10 (excellent).")
    #
    # from transformers import AutoTokenizer, AutoModelForCausalLM
    # import transformers
    # import torch
    #
    #
    # model = "tiiuae/falcon-7b-instruct"
    #
    # tokenizer = AutoModelForCausalLM.from_pretrained(model, device_map="auto", offload_folder="offload", trust_remote_code = True)
    # pipeline = transformers.pipeline(
    #     "text-generation",
    #     model = model,
    #     tokenizer = tokenizer,
    #     torch_dtype = torch.bfloat16,
    #     trust_remote_code = True,
    #     device_map = "auto",
    #     offload_folder = "offload",
    # )
    # sequences = pipeline(
    #     "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
    #     max_length = 200,
    #     do_sample = True,
    #     top_k = 10,
    #     num_return_sequences = 1,
    #     eos_token_id = tokenizer.eos_token_id,
    # )
    #
    # for seq in sequences:
    #     print(seq)

