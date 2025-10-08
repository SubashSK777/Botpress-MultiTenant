import gradio as gr

# Define a custom theme based on Soft theme for a modern/Apple aesthetic
# Using indigo for a deep tech blue (Tencent blue approximation)
APPLE_TENCENT_THEME = gr.themes.Soft(
    primary_hue=gr.themes.colors.indigo, # FIX: Corrected capitalization to lowercase 'indigo'
    secondary_hue=gr.themes.colors.gray,
    neutral_hue=gr.themes.colors.neutral,
    spacing_size=gr.themes.sizes.spacing_lg,
    radius_size=gr.themes.sizes.radius_lg,
    text_size=gr.themes.sizes.text_md,
).set(
    # Custom tweaks for a cleaner, high-contrast look (Apple/Modern aesthetic)
    body_background_fill="#F9F9F9",
    background_fill_primary="#FFFFFF",
    background_fill_secondary="#F0F0F0",
    shadow_drop="0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px 0 rgba(0, 0, 0, 0.02)",
    shadow_drop_lg="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
    button_primary_background_fill="*primary_500",
    button_primary_background_fill_hover="*primary_600",
)