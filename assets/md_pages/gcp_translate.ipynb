{
 "cells": [
  {
   "cell_type": "markdown",
   "source": [
    "# Translate Kaizen Data using Google Cloud Platform"
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "source": [
    "# import packages\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os\n",
    "import json\n",
    "from google.cloud import translate\n",
    "\n",
    "### free but extremely slow method to translate\n",
    "# from deep_translator import GoogleTranslator\n",
    "# to_translate = \"Bonjour\"\n",
    "# translated = GoogleTranslator(source=\"auto\", target=\"en\").translate(to_translate)\n",
    "# translated"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "# GCP client credentials\n",
    "client_credentials = json.load(open(\"/Users/purushottam/Dropbox (Good Business Lab)/Purushottam/translate-seagate-348b9248f1ec.json\"))\n",
    "\n",
    "# set project id and build client\n",
    "project_id = client_credentials['project_id']\n",
    "assert project_id\n",
    "parent = f\"projects/{project_id}\"\n",
    "client = translate.TranslationServiceClient()"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "# Get all languages\n",
    "response = client.get_supported_languages(parent=parent, display_language_code=\"en\")\n",
    "languages = response.languages\n",
    "\n",
    "print(f\" Languages: {len(languages)} \".center(60, \"-\"))\n",
    "for language in languages:\n",
    "    print(f\"{language.language_code}\\t{language.display_name}\")"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "# GCP translate\n",
    "sample_text = [\"Bonjour\", \"Oui\"]\n",
    "target_language_code = \"en\"\n",
    "\n",
    "response = client.translate_text(\n",
    "    contents= sample_text,\n",
    "    target_language_code=target_language_code,\n",
    "    parent=parent,\n",
    ")\n",
    "\n",
    "for translation in response.translations:\n",
    "    print(translation.translated_text)"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "# Load Raw Data\n",
    "df = pd.read_stata(\"/Volumes/PII_PRECL/pii_kaizen_updated.dta\")"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "# set empty translated output list\n",
    "translated_output_list = []"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "x1 = 0\n",
    "x2 = x1 + 10"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "source": [
    "# set subset of raw file\n",
    "input_df = df[140000:145000].copy(deep=True)\n",
    "# remove line separators from data\n",
    "input_df = input_df.replace(r'\\r', '', regex=True)\n",
    "input_df = input_df.replace(r'\\n', '', regex=True)"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "# translate text\n",
    "# Translate All Thai Columns\n",
    "#varnames_th = ['project_name', 'project_need', 'project_idea', 'project_countermeasure', 'project_result', 'project_expansion', 'employee_benefit', 'customer_benefit', 'org_benefit', 'social_benefit']\n",
    "var = 'project_name'\n",
    "var_th = var + '_thai'\n",
    "var_en = var + '_en'\n",
    "\n",
    "input_text = input_df[var_th]\n",
    "target_language_code = \"en\"\n",
    "\n",
    "response = client.translate_text(\n",
    "    contents = input_text,\n",
    "    target_language_code = target_language_code,\n",
    "    parent = parent,\n",
    ")\n",
    "\n",
    "for n in range(0,len(response.translations)):\n",
    "    translated_output = response.translations[n].translated_text\n",
    "    translated_output_list.append(translated_output)"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "source": [
    "# Batch Translation\n",
    "x1 = 0\n",
    "x2 = 200\n",
    "\n",
    "var = 'project_name'\n",
    "var_th = var + '_thai'\n",
    "var_en = var + '_en'\n",
    "\n",
    "# GCP translate API doesn't support empty strings (to avoid errors)\n",
    "# input_df['proj_name_empty'] = np.where(input_df[var_th] == \"\", 1, 0)\n",
    "input_df[var_th] = np.where(input_df[var_th] == \"\", \"Oui\", input_df[var_th])\n",
    "# doesn't support strings which are too long\n",
    "#input_df['str_len'] = input_df[var_th].str.len()\n",
    "input_df[var_th] = np.where(input_df[var_th].str.len() >= 200, \"Non\", input_df[var_th])\n",
    "\n",
    "translated_output_list = []\n",
    "\n",
    "while x1 < len(input_df):\n",
    "    input_text = input_df[x1:x2][var_th]\n",
    "    target_language_code = \"en\"\n",
    "    # translate \n",
    "    response = client.translate_text(\n",
    "    contents = input_text,\n",
    "    target_language_code = target_language_code,\n",
    "    parent = parent,\n",
    "    )\n",
    "    # append to list\n",
    "    for n in range(0,len(response.translations)):\n",
    "        translated_output = response.translations[n].translated_text\n",
    "        translated_output_list.append(translated_output)\n",
    "    # update counter\n",
    "    x1 = x1 + 200\n",
    "    x2 = x1 + 200"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "source": [],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "source": [
    "# set new translated variable\n",
    "input_df[var_en] = translated_output_list\n",
    "# export data\n",
    "input_df.to_csv(path_or_buf = \"/Users/purushottam/Downloads/pii_kaizen_updated_translated_\" + var + \".csv\", sep=\",\", header=True, mode='w+')"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "sys.getsizeof(input_text[1:1000])"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "# set subset of raw file\n",
    "input_df = df[0:10].copy(deep=True)\n",
    "# remove line separators from data\n",
    "input_df = input_df.replace(r'\\r', '', regex=True)\n",
    "input_df = input_df.replace(r'\\n', '', regex=True)\n",
    "\n",
    "# Translate All Thai Columns\n",
    "#varnames_th = ['project_name', 'project_need', 'project_idea', 'project_countermeasure', 'project_result', 'project_expansion', 'employee_benefit', 'customer_benefit', 'org_benefit', 'social_benefit']\n",
    "varnames_th = ['project_name']\n",
    "\n",
    "for var in varnames_th:\n",
    "    # thai var names\n",
    "    var_th = var + \"_thai\"\n",
    "    # translate using GoogleTranslator package\n",
    "    output_text_list = []\n",
    "    for n in range(len(input_df)):\n",
    "        to_translate = input_df[var_th][n]\n",
    "        output = GoogleTranslator(source=\"auto\", target=\"en\").translate(to_translate)\n",
    "        output_text_list.append(output)\n",
    "    # variable name english\n",
    "    var_en = var + \"_en\"\n",
    "    # add translated text to data\n",
    "    input_df[var_en] = output_text_list\n"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "input_df[\"project_name_en\"]"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "# export data\n",
    "input_df.to_csv(path_or_buf = \"/Users/purushottam/Downloads/pii_kaizen_updated_translated_\" + var + \".csv\", sep=\",\", header=True, mode='w+')"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "source": [
    "len(output_text_list)"
   ],
   "outputs": [],
   "metadata": {}
  }
 ],
 "metadata": {
  "orig_nbformat": 4,
  "language_info": {
   "name": "python",
   "version": "3.9.1",
   "mimetype": "text/x-python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "pygments_lexer": "ipython3",
   "nbconvert_exporter": "python",
   "file_extension": ".py"
  },
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.9.1 64-bit"
  },
  "interpreter": {
   "hash": "4cd7ab41f5fca4b9b44701077e38c5ffd31fe66a6cab21e0214b68d958d0e462"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}