
Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      MoveUnit(All, "60 + 1n Hydralisk", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
   },
}




for i = 0, 5, 1 do

x = 150 - 30 * i;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y, x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y, -x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 100 - 20 * i;
y = 100 - 20 * i;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y, x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y, -x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 12, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

x = 150;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y, x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y, -x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 100;
y = 100;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y, x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y, -x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, SetTo, 2, " `SkillLoop3");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      Wait(200);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 150;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Guardian", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y, x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y, -x);
      MoveUnit(1, "80 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

x = 100;
y = 100;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Mutalisk", "[Skill]Unit_Wait_8", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, x, y);
      MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -x, -y);
      MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, -y, x);
      MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(175, y, -x);
      MoveUnit(1, "80 + 1n Mutalisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, SetTo, 3, " `SkillLoop3");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      Wait(1100);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(16, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "60 + 1n Hydralisk", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "60 + 1n Hydralisk", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "60 + 1n Hydralisk", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "60 + 1n Hydralisk", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "60 + 1n Hydralisk", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(160);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(360);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 5, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(16, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(160);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(300);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 7, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(16, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "50 + 1n Tank", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "50 + 1n Tank", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "50 + 1n Tank", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "50 + 1n Tank", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "20.EmetSelch");
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(360);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

for i = 0, 7, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 9, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(16, "80 + 1n Tank", "[Skill]Unit_Wait_8", CurrentPlayer);  
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(4, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 17, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(300);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

interval = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, i + 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "80 + 1n Guardian", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
      LMove(175, 0, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


for i = 0, 3, 1 do

interval = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "80 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "80 + 1n Guardian", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
      LMove(175, -interval, interval);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -2 * interval, -interval);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -2 * interval, -interval);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 2 * i + 2, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "80 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "80 + 1n Guardian", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
      LMove(175, -interval, interval);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -2 * interval, -interval);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -2 * interval, -interval);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}



for i = 0, 3, 1 do

interval = 32;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "40 + 1n Guardian", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "80 + 1n Guardian", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "80 + 1n Guardian", "Anywhere", CurrentPlayer);
      LMove(175, -interval, interval);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -2 * interval, -interval);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -2 * interval, -interval);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 2 * i + 2, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "40 + 1n Guardian", "[Skill]Unit_Wait_7", CurrentPlayer);  
      CreateUnit(4, "60 + 1n Hydralisk", "[Skill]Unit_Wait_7", CurrentPlayer);  
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("20.EmetSelch", "80 + 1n Mutalisk", CurrentPlayer, "Anywhere");
      RemoveUnitAt(1, "80 + 1n Mutalisk", "Anywhere", CurrentPlayer);
      LMove(175, -interval, interval);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -2 * interval, -interval);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, -2 * interval, -interval);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      LMove(175, interval, 0);
      MoveUnit(1, "40 + 1n Guardian", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      MoveLocation("20.EmetSelch", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "60 + 1n Hydralisk", CurrentPlayer, "[Skill]Unit_Wait_ALL", "20.EmetSelch");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop3");
      Deaths(CurrentPlayer, Exactly, 9, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Guardian", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}





Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 3000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 120, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}