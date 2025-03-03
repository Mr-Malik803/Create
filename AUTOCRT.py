try:
    import AUTRT
    print("✅ Module 'AUTRT' imported successfully!")

    print("▶️ Running main function...")
    AUTRT.main()  # Assumes 'main' exists; will raise an error if it doesn't.

except ImportError as e:
    print("❌ Import error:", e)

except AttributeError:
    print("⚠️ 'main' function not found. Check available attributes:", dir(AUTCRT))
