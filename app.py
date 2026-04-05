# imports
import streamlit as st
import json

from prompt import build_prompt
from llm_handler import analyze

# title
st.title("Debate Fact Checker")

# input box
text = st.text_area("Enter debate text")

# button
if st.button("Analyze"):

    # check if empty
    if text.strip() == "":
        st.write("enter some text first")

    else:
        st.write("processing...")

        # build prompt
        prompt = build_prompt(text)

        # send to model
        result = analyze(prompt)

        # try to read json properly
        # trying to extract json properly
try:
    start = result.find("{")
    end = result.rfind("}") + 1

    clean_json = result[start:end]

    data = json.loads(clean_json)

    # loop through speakers
    for speaker in data["speakers"]:

        st.subheader(speaker["name"])

        score = speaker["score"]

        # show score
        st.write("Score:", score)

        # small visual indicator
        if score >= 0.7:
            st.success("High accuracy")

        elif score >= 0.4:
            st.warning("Moderate accuracy")

        else:
            st.error("Low accuracy")

        st.write("Claims:")

        # loop through claims
        for item in speaker["claims"]:

            st.write("•", item["claim"])

            verdict = item["verdict"]

            if verdict == "TRUE":
                st.success(verdict)

            elif verdict == "FALSE":
                st.error(verdict)

            else:
                st.warning(verdict)

            st.write(item["explanation"])
            st.write("---")

except:
    st.write("could not parse properly, raw output below:")
    st.write(result)