init -990 python in mas_submod_utils:
    Submod(
        author="Otter",
        name="Otter farewells",
        description="New 'Goodbye' options.",
        version="1.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Otter's farewells",
            user_name="my-otter-self",
            repository_name="otter_MAS_farewells",
            submod_dir="/Submods/Otter's farewells",
            extraction_depth=3,
            redirected_files=(
                "README.md",
            )
        )
