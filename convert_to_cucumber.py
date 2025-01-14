import json

def convert_behave_to_cucumber(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        behave_data = json.load(f)

    cucumber_data = []
    for feature in behave_data:
        cucumber_feature = {
            "uri": feature.get("location", "").split(":")[0],  # Usar solo el nombre del archivo
            "id": feature["name"].lower().replace(" ", "-"),
            "keyword": feature["keyword"],
            "name": feature["name"],
            "line": int(feature["location"].split(":")[1]) if ":" in feature["location"] else 1,
            "description": "\n".join(feature.get("description", [])),
            "elements": []
        }
        
        for scenario in feature.get("elements", []):
            cucumber_scenario = {
                "keyword": scenario["keyword"],
                "name": scenario["name"],
                "line": int(scenario["location"].split(":")[1]) if ":" in scenario["location"] else 1,
                "type": scenario["type"],
                "steps": []
            }
            for step in scenario.get("steps", []):
                cucumber_step = {
                    "keyword": step["keyword"] + " ",
                    "name": step["name"],
                    "line": int(step["location"].split(":")[1]) if ":" in step["location"] else 1,
                    "result": {
                        "status": step["result"]["status"],
                        "duration": step["result"].get("duration", 0)
                    }
                }
                cucumber_scenario["steps"].append(cucumber_step)
            cucumber_scenario["tags"] = [{"name": tag} for tag in scenario.get("tags", [])]
            cucumber_feature["elements"].append(cucumber_scenario)
        
        cucumber_feature["tags"] = [{"name": tag} for tag in feature.get("tags", [])]
        cucumber_data.append(cucumber_feature)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cucumber_data, f, indent=2, ensure_ascii=False)

# Uso del script
convert_behave_to_cucumber("resultados.json", "cucumber-results.json")
