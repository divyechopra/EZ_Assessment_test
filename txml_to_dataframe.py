import xml.etree.ElementTree as ET
import pandas as pd

def convert_tmx_to_dataframe(input_file_path, output_csv_path):
    try:
        # Parse the XML file
        tree = ET.parse(input_file_path)
        root = tree.getroot()

        # Use list comprehensions to extract data
        data = [
            {'Language': tuv.get('{http://www.w3.org/XML/1998/namespace}lang'), 'Text': tuv.find('./seg').text}
            for tu in root.findall('.//tu')
            for tuv in tu.findall('./tuv')
        ]

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        df.to_csv(output_csv_path, index=False)

        print("Conversion completed successfully.")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
