import streamlit as st
import requests
from datetime import datetime

# Skincare knowledge base
skincareKnowledge = {
    "acne": {
        "description": "Acne is a common skin condition that occurs when hair follicles become clogged with oil and dead skin cells, leading to pimples, blackheads, or whiteheads.",
        "remedies": [
            "Cleanse your face twice daily with a gentle, non-comedogenic cleanser",
            "Use products containing benzoyl peroxide, salicylic acid, or retinoids",
            "Avoid touching your face and picking at pimples",
            "Change pillowcases regularly",
            "Keep hair products away from your face"
        ],
        "diet": [
            "Reduce consumption of high-glycemic foods like white bread and sugary snacks",
            "Limit dairy if you notice it triggers breakouts",
            "Increase intake of zinc-rich foods (pumpkin seeds, nuts)",
            "Eat more omega-3 fatty acids (found in fish, flaxseeds)",
            "Stay hydrated with plenty of water"
        ],
        "products": [
            "Gentle cleansers like CeraVe Foaming Facial Cleanser or La Roche-Posay Effaclar",
            "Treatment products with 2% salicylic acid or 2.5-5% benzoyl peroxide",
            "Non-comedogenic moisturizers",
            "Oil-free sunscreen with at least SPF 30",
            "Spot treatments containing tea tree oil or sulfur"
        ],
        "ingredients_to_look_for": [
            "Salicylic acid",
            "Benzoyl peroxide",
            "Niacinamide",
            "Retinol",
            "Tea tree oil",
            "Sulfur"
        ],
        "ingredients_to_avoid": [
            "Coconut oil",
            "Lanolin",
            "Isopropyl myristate",
            "Heavy oils",
            "Sodium lauryl sulfate"
        ]
    },
    "dryness": {
        "description": "Dry skin lacks moisture and can feel tight, rough, and sometimes flaky or itchy. It may be genetic or caused by environmental factors like weather or harsh products.",
        "remedies": [
            "Take shorter showers using lukewarm (not hot) water",
            "Apply moisturizer immediately after bathing while skin is still damp",
            "Use a humidifier in dry environments",
            "Avoid harsh soaps and cleansers",
            "Limit exfoliation to 1-2 times per week"
        ],
        "diet": [
            "Increase consumption of omega-3 fatty acids (salmon, walnuts, flaxseeds)",
            "Eat foods rich in vitamin E (avocados, nuts, seeds)",
            "Consume more water-rich fruits and vegetables",
            "Consider collagen-boosting foods like bone broth",
            "Stay well-hydrated throughout the day"
        ],
        "products": [
            "Cream or oil-based cleansers like Cetaphil Gentle Skin Cleanser",
            "Hyaluronic acid serums to boost hydration",
            "Rich moisturizers containing ceramides, shea butter, or squalane",
            "Overnight hydrating masks",
            "Facial oils such as rosehip, jojoba, or argan oil"
        ],
        "ingredients_to_look_for": [
            "Hyaluronic acid",
            "Glycerin",
            "Ceramides",
            "Shea butter",
            "Squalane",
            "Niacinamide"
        ],
        "ingredients_to_avoid": [
            "Alcohol denat",
            "Fragrances",
            "Sodium lauryl sulfate",
            "Menthol",
            "Eucalyptus"
        ]
    },
    "aging": {
        "description": "Skin aging includes concerns like fine lines, wrinkles, loss of elasticity, and uneven skin tone caused by both intrinsic aging and environmental factors.",
        "remedies": [
            "Use sunscreen daily (SPF 30 or higher)",
            "Develop a consistent skincare routine with antioxidants",
            "Get adequate sleep (7-9 hours nightly)",
            "Practice stress management techniques",
            "Avoid smoking and limit alcohol consumption"
        ],
        "diet": [
            "Consume antioxidant-rich foods (berries, dark leafy greens)",
            "Eat foods high in vitamin C (citrus fruits, bell peppers)",
            "Include collagen-supporting proteins",
            "Stay hydrated to maintain skin plumpness",
            "Limit sugar and processed foods that can cause inflammation"
        ],
        "products": [
            "Retinol or prescription retinoids to boost cell turnover",
            "Vitamin C serums for brightening and collagen production",
            "Peptide creams to improve firmness",
            "Chemical exfoliants with AHAs or BHAs",
            "Hydrating products with hyaluronic acid"
        ],
        "ingredients_to_look_for": [
            "Retinol/Retinoids",
            "Vitamin C",
            "Peptides",
            "Niacinamide",
            "AHAs (glycolic acid, lactic acid)",
            "Coenzyme Q10"
        ],
        "ingredients_to_avoid": [
            "High concentrations of fragrances",
            "Drying alcohols",
            "Harsh physical exfoliants"
        ]
    },
    "sensitivity": {
        "description": "Sensitive skin reacts easily to products or environmental factors with redness, irritation, burning, or itching. It may be temporary or chronic.",
        "remedies": [
            "Patch test all new products before full application",
            "Simplify your skincare routine with fewer products",
            "Avoid fragranced products and common irritants",
            "Protect skin from extreme temperatures and wind",
            "Keep a journal to identify triggers"
        ],
        "diet": [
            "Focus on anti-inflammatory foods (turmeric, ginger, fatty fish)",
            "Consider potential food sensitivities that may manifest on skin",
            "Stay hydrated to maintain your skin barrier",
            "Include foods rich in omega-3 fatty acids",
            "Consume prebiotics and probiotics for gut-skin health"
        ],
        "products": [
            "Fragrance-free, hypoallergenic cleansers",
            "Barrier-repairing moisturizers with ceramides",
            "Mineral-based sunscreens with zinc oxide or titanium dioxide",
            "Products labeled for sensitive skin with minimal ingredients",
            "Centella asiatica (cica) or oat-based soothing products"
        ],
        "ingredients_to_look_for": [
            "Centella asiatica (cica)",
            "Colloidal oatmeal",
            "Aloe vera",
            "Ceramides",
            "Allantoin",
            "Bisabolol"
        ],
        "ingredients_to_avoid": [
            "Fragrances",
            "Essential oils",
            "Alcohol",
            "Sulfates",
            "Chemical sunscreen filters",
            "Strong acids"
        ]
    },
    "hyperpigmentation": {
        "description": "Hyperpigmentation includes dark spots, patches, or uneven skin tone caused by excess melanin production due to sun damage, inflammation, or hormonal changes.",
        "remedies": [
            "Always wear broad-spectrum sunscreen (essential)",
            "Use protective clothing and seek shade",
            "Be gentle with skin to avoid post-inflammatory darkening",
            "Treat any underlying conditions like acne or hormonal issues",
            "Be patient - treatment requires consistency and time"
        ],
        "diet": [
            "Consume foods rich in vitamin C (helps inhibit melanin production)",
            "Include foods with vitamin E for antioxidant protection",
            "Eat foods with lycopene (tomatoes, watermelon)",
            "Consider foods with glutathione precursors",
            "Stay hydrated for overall skin health"
        ],
        "products": [
            "Vitamin C serums (10-20%)",
            "Products with niacinamide (vitamin B3)",
            "Alpha arbutin or kojic acid serums",
            "Exfoliants with glycolic or lactic acid",
            "Prescription treatments like hydroquinone or tretinoin"
        ],
        "ingredients_to_look_for": [
            "Vitamin C",
            "Niacinamide",
            "Alpha arbutin",
            "Kojic acid",
            "Tranexamic acid",
            "Glycolic acid",
            "Lactic acid"
        ],
        "ingredients_to_avoid": [
            "Fragrances that might cause irritation",
            "Harsh physical scrubs",
            "Potential photosensitizing ingredients without proper sun protection"
        ]
    },
    "rosacea": {
        "description": "Rosacea is a chronic inflammatory skin condition causing facial redness, visible blood vessels, and sometimes bumps or swelling. It may flare in response to triggers.",
        "remedies": [
            "Identify and avoid personal triggers (spicy foods, alcohol, extreme temperatures)",
            "Use gentle, non-irritating skincare products",
            "Protect skin from sun exposure with broad-spectrum SPF",
            "Apply cool compresses to reduce flare-ups",
            "Consider LED light therapy (blue and red light)"
        ],
        "diet": [
            "Avoid common trigger foods (spicy foods, hot beverages, alcohol)",
            "Include anti-inflammatory omega-3 rich foods",
            "Consider a food journal to identify personal triggers",
            "Stay well-hydrated throughout the day",
            "Consume foods rich in zinc and vitamin B"
        ],
        "products": [
            "Gentle, fragrance-free cleansers",
            "Centella asiatica (cica) or green tea products",
            "Azelaic acid treatment products",
            "Mineral-based sunscreens",
            "Soothing moisturizers with ceramides"
        ],
        "ingredients_to_look_for": [
            "Azelaic acid",
            "Centella asiatica",
            "Green tea extract",
            "Niacinamide",
            "Ceramides",
            "Aloe vera"
        ],
        "ingredients_to_avoid": [
            "Alcohol",
            "Fragrances",
            "Witch hazel",
            "Menthol",
            "Camphor",
            "Sodium lauryl sulfate"
        ]
    },
    "eczema": {
        "description": "Eczema (atopic dermatitis) is a chronic condition causing dry, itchy, and inflamed skin. It's often related to genetics and immune system dysfunction.",
        "remedies": [
            "Take lukewarm (not hot) showers limited to 10 minutes",
            "Apply moisturizer immediately after bathing",
            "Identify and avoid triggers (certain fabrics, detergents, stress)",
            "Use a humidifier in dry environments",
            "Wear loose-fitting, cotton clothing"
        ],
        "diet": [
            "Consider potential food sensitivities (dairy, eggs, gluten)",
            "Include anti-inflammatory omega-3 fatty acids",
            "Consume probiotic-rich foods for gut-skin health",
            "Stay well-hydrated throughout the day",
            "Include foods rich in vitamin E"
        ],
        "products": [
            "Fragrance-free, gentle cleansers",
            "Moisturizers with ceramides or colloidal oatmeal",
            "Barrier repair creams",
            "Products containing 1% hydrocortisone for flare-ups (short-term use)",
            "Mineral-based sunscreens designed for sensitive skin"
        ],
        "ingredients_to_look_for": [
            "Colloidal oatmeal",
            "Ceramides",
            "Glycerin",
            "Shea butter",
            "Aloe vera",
            "Panthenol"
        ],
        "ingredients_to_avoid": [
            "Fragrances",
            "Essential oils",
            "Lanolin (for some people)",
            "Cocamidopropyl betaine",
            "Propylene glycol",
            "Formaldehyde releasers"
        ]
    },
    "general": {
        "description": "General skincare principles apply to maintaining healthy skin regardless of specific concerns.",
        "tips": [
            "Cleanse your face morning and night",
            "Always remove makeup before sleeping",
            "Use sunscreen daily (SPF 30+) regardless of weather",
            "Stay hydrated by drinking plenty of water",
            "Get adequate sleep (7-9 hours nightly)",
            "Eat a balanced diet rich in antioxidants and omega-3s",
            "Avoid touching your face throughout the day",
            "Change pillowcases 1-2 times per week",
            "Manage stress through regular exercise, meditation, or other techniques",
            "Clean makeup brushes and tools regularly"
        ],
        "routine": [
            "Morning: Gentle cleanser → Treatment product → Moisturizer → Sunscreen",
            "Evening: Makeup remover (if needed) → Cleanser → Treatment product → Moisturizer",
            "1-2x weekly: Gentle exfoliation",
            "1-2x weekly: Treatment mask appropriate for your skin type"
        ],
        "products": [
            "Basic gentle cleanser suitable for your skin type",
            "Alcohol-free toner (optional)",
            "Moisturizer suited to your skin needs",
            "Broad-spectrum sunscreen SPF 30+",
            "Weekly exfoliant appropriate for your skin"
        ]
    }
}

# Configuration for Open Beauty Facts API
API_BASE_URL = 'https://world.openbeautyfacts.org/api/v0'

def search_products(query, category=None):
    try:
        search_url = f"{API_BASE_URL}/search?search_terms={query}&json=true"
        
        if category:
            search_url += f"&tagtype_0=categories&tag_contains_0=contains&tag_0={category}"
        
        search_url += '&fields=product_name,brands,ingredients_text,image_url&page_size=5'
        
        response = requests.get(search_url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Error searching products: {e}")
        return None

def search_knowledge(query):
    normalized_query = query.lower()
    
    # First check for synonyms and specific terms
    concern_synonyms = {
        'acne': ['pimple', 'pimples', 'breakout', 'breakouts', 'zits'],
        'dryness': ['dry skin', 'flaky skin', 'dehydrated skin'],
        'aging': ['wrinkle', 'wrinkles', 'fine lines', 'anti-aging'],
        'sensitivity': ['sensitive skin', 'irritated skin', 'redness'],
        'hyperpigmentation': ['dark spots', 'uneven tone', 'melasma'],
        'rosacea': ['facial redness', 'flushing'],
        'eczema': ['dermatitis', 'itchy skin']
    }
    
    # Check if query contains any synonym
    for concern, synonyms in concern_synonyms.items():
        if any(synonym in normalized_query for synonym in [concern] + synonyms):
            # Check if concern exists in knowledge base
            if concern in skincareKnowledge:
                return {"concern": concern, "info": skincareKnowledge[concern]}
            else:
                return None
    
    # Rest of your function remains the same...
    if any(word in normalized_query for word in ['product', 'recommend', 'buy', 'use']):
        for concern, info in skincareKnowledge.items():
            if concern != 'general' and concern in normalized_query:
                return {"concern": concern, "info": info, "requestType": "product"}
    
    if any(word in normalized_query for word in ['ingredient', 'contain']):
        return {"requestType": "ingredient", "query": normalized_query}
    
    if any(word in normalized_query for word in ['routine', 'basics', 'tips', 'hello', 'hi', 'start']):
        return {"concern": "general", "info": skincareKnowledge["general"]}
    
    return None
def extract_ingredients(query):
    common_ingredients = [
        'retinol', 'vitamin c', 'hyaluronic acid', 'niacinamide', 'salicylic acid',
        'benzoyl peroxide', 'azelaic acid', 'glycolic acid', 'lactic acid',
        'ceramides', 'peptides', 'squalane', 'centella', 'tea tree'
    ]
    
    for ingredient in common_ingredients:
        if ingredient in query.lower():
            return ingredient
    return None

def format_product_results(data):
    if not data or not data.get('products'):
        return "I couldn't find any specific products matching your query."
    
    response = "### Product Recommendations\n"
    for product in data['products'][:5]:  # Limit to 5 products
        if product.get('product_name'):
            response += f"**{product['product_name']}**\n"
            if product.get('brands'):
                response += f"Brand: {product['brands']}\n"
            if product.get('ingredients_text'):
                ingredients = product['ingredients_text'][:200] + '...' if len(product['ingredients_text']) > 200 else product['ingredients_text']
                response += f"Ingredients: {ingredients}\n"
            response += "\n"
    
    response += "\n*Note: Always patch test new products and consult a dermatologist for serious concerns.*"
    return response

def format_response(search_result):
    if not search_result:
        return "I can help with acne, dryness, aging, sensitivity, hyperpigmentation, rosacea, or eczema. Could you rephrase your question?"
    
    if search_result.get("requestType") == "ingredient":
        ingredient = extract_ingredients(search_result["query"])
        if not ingredient:
            return "Which specific ingredient are you asking about?"
        
        response = f"### Information About {ingredient.title()}\n"
        
        concerns = [concern for concern, info in skincareKnowledge.items() 
                   if concern != "general" and "ingredients_to_look_for" in info
                   and any(ing.lower() == ingredient 
                   for ing in info.get('ingredients_to_look_for', []))]
        
        if concerns:
            response += f"{ingredient.title()} helps with: {', '.join(concerns)}\n\n"
            
            ingredient_info = {
                'retinol': "Promotes skin cell turnover. Start with low concentrations (0.25-0.5%).",
                'vitamin c': "Brightens skin and boosts collagen. Look for 10-20% concentrations.",
                'hyaluronic acid': "Excellent hydrator. Apply to damp skin for best results.",
                'niacinamide': "Improves barrier function and reduces redness. Works well in 2-5% concentrations.",
                'salicylic acid': "Clears pores. Effective in 0.5-2% concentrations."
            }.get(ingredient.lower())
            
            response += ingredient_info if ingredient_info else f"{ingredient.title()} is a beneficial skincare ingredient."
        else:
            response += f"Would you like me to search for products containing {ingredient}?"
        
        return response
    
    concern = search_result.get("concern")
    info = search_result.get("info")
    
    if not concern or not info:
        return "I couldn't find information about that specific concern."
    
    if concern == "general":
        response = "### General Skincare Advice\n\n"
        response += "\n".join(f"- {tip}" for tip in info.get("tips", [])) + "\n\n"
        response += "### Recommended Routine\n"
        response += "\n".join(f"- {step}" for step in info.get("routine", []))
    else:
        response = f"### {concern.title()} Care Guide\n\n"
        response += f"{info.get('description', 'No description available.')}\n\n"
        
        if "remedies" in info:
            response += "#### Recommended Remedies\n"
            response += "\n".join(f"- {remedy}" for remedy in info["remedies"]) + "\n\n"
        
        if "products" in info:
            response += "#### Recommended Products\n"
            response += "\n".join(f"- {product}" for product in info["products"])
        else:
            response += "\n*No specific product recommendations available for this concern.*\n"
    
    return response

    if not search_result:
        return "I can help with acne, dryness, aging, sensitivity, hyperpigmentation, rosacea, or eczema. Could you rephrase your question?"
    
    if search_result.get("requestType") == "ingredient":
        ingredient = extract_ingredients(search_result["query"])
        if not ingredient:
            return "Which specific ingredient are you asking about?"
        
        response = f"### Information About {ingredient.title()}\n"
        
        concerns = [concern for concern, info in skincareKnowledge.items() 
                   if concern != "general" and any(ing.lower() == ingredient 
                   for ing in info.get('ingredients_to_look_for', []))]
        
        if concerns:
            response += f"{ingredient.title()} helps with: {', '.join(concerns)}\n\n"
            
            # Add specific info about common ingredients
            ingredient_info = {
                'retinol': "Promotes skin cell turnover. Start with low concentrations (0.25-0.5%).",
                'vitamin c': "Brightens skin and boosts collagen. Look for 10-20% concentrations.",
                'hyaluronic acid': "Excellent hydrator. Apply to damp skin for best results.",
                'niacinamide': "Improves barrier function and reduces redness. Works well in 2-5% concentrations.",
                'salicylic acid': "Clears pores. Effective in 0.5-2% concentrations."
            }.get(ingredient.lower())
            
            response += ingredient_info if ingredient_info else f"{ingredient.title()} is a beneficial skincare ingredient."
        else:
            response += f"Would you like me to search for products containing {ingredient}?"
        
        return response
    
    concern = search_result.get("concern")
    info = search_result.get("info")
    
    if not concern or not info:
        return "I couldn't find information about that specific concern."
    
    if concern == "general":
        response = "### General Skincare Advice\n\n"
        response += "\n".join(f"- {tip}" for tip in info["tips"]) + "\n\n"
        response += "### Recommended Routine\n"
        response += "\n".join(f"- {step}" for step in info["routine"])
    else:
        response = f"### {concern.title()} Care Guide\n\n"
        response += f"{info['description']}\n\n"
        response += "#### Recommended Remedies\n"
        response += "\n".join(f"- {remedy}" for remedy in info["remedies"]) + "\n\n"
        response += "#### Recommended Products\n"
        response += "\n".join(f"- {product}" for product in info["products"])
    
    return response

def main():
    st.set_page_config(page_title="Skincare Chatbot", page_icon="💆‍♀️")
    
    st.title("💆‍♀️ Skincare Chatbot")
    st.caption("With Open Beauty Facts API Integration")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hello! I'm your Skincare Assistant. I can help with concerns like acne, dryness, aging, sensitivity, and more. What's your skincare question today?"
        }]
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if prompt := st.chat_input("Ask about your skin concerns..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                search_result = search_knowledge(prompt)
                
                # If asking about products/ingredients, try API search
                if search_result and search_result.get("requestType") in ["product", "ingredient"]:
                    search_term = None
                    if search_result["requestType"] == "product":
                        ingredients = search_result["info"]["ingredients_to_look_for"]
                        search_term = ingredients[0] if ingredients else None
                    else:
                        search_term = extract_ingredients(search_result["query"])
                    
                    if search_term:
                        api_result = search_products(search_term)
                        if api_result and api_result.get("products"):
                            response = format_product_results(api_result)
                        else:
                            response = format_response(search_result)
                    else:
                        response = format_response(search_result)
                else:
                    response = format_response(search_result)
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()