import Function as f;

const s = StringBuffer();

function main(cp)
{
   MoveLocation("23.Mayuri_Bozo", f.heroID[cp], cp, "Anywhere");
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {                        
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");
            SetSwitch("Recall - Mayuri", Set);

            f.SkillWait(cp, 1600);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.Voice_Routine(cp, 4);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 8)
         {         
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.DotShape(cp, 1, " Creep. Dunkelheit", 25, 175 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, " Creep. Dunkelheit", 75, 175 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, " Creep. Dunkelheit", 125, 175 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, " Creep. Dunkelheit", 175, 175 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, " Creep. Dunkelheit", -25, -175 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, " Creep. Dunkelheit", -75, -175 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, " Creep. Dunkelheit", -125, -175 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, " Creep. Dunkelheit", -175, -175 + 50 * f.loop[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
            
            f.DotShape(cp, 1, "40 + 1n Mojo", 25, 175 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Mojo", 75, 175 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Mojo", 125, 175 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Mojo", 175, 175 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Mojo", -25, -175 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Mojo", -75, -175 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Mojo", -125, -175 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, "40 + 1n Mojo", -175, -175 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", 25, 225 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", 75, 225 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", 125, 225 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", 175, 225 - 50 * f.loop[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -25, -225 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -75, -225 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -125, -225 + 50 * f.loop[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -175, -225 + 50 * f.loop[cp]);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.SkillWait(cp, 1040);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 8)
         {         
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.DotShape(cp, 1, " Creep. Dunkelheit", 175 - 50 * f.loop[cp], 25);
            f.DotShape(cp, 1, " Creep. Dunkelheit", 175 - 50 * f.loop[cp], 75);
            f.DotShape(cp, 1, " Creep. Dunkelheit", 175 - 50 * f.loop[cp], 125);
            f.DotShape(cp, 1, " Creep. Dunkelheit", 175 - 50 * f.loop[cp], 175);
            f.DotShape(cp, 1, " Creep. Dunkelheit", -175 + 50 * f.loop[cp], -25);
            f.DotShape(cp, 1, " Creep. Dunkelheit", -175 + 50 * f.loop[cp], -75);
            f.DotShape(cp, 1, " Creep. Dunkelheit", -175 + 50 * f.loop[cp], -125);
            f.DotShape(cp, 1, " Creep. Dunkelheit", -175 + 50 * f.loop[cp], -175);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);

            f.DotShape(cp, 1, "40 + 1n Mojo", 175 - 50 * f.loop[cp], 25);
            f.DotShape(cp, 1, "40 + 1n Mojo", 175 - 50 * f.loop[cp], 75);
            f.DotShape(cp, 1, "40 + 1n Mojo", 175 - 50 * f.loop[cp], 125);
            f.DotShape(cp, 1, "40 + 1n Mojo", 175 - 50 * f.loop[cp], 175);
            f.DotShape(cp, 1, "40 + 1n Mojo", -175 + 50 * f.loop[cp], -25);
            f.DotShape(cp, 1, "40 + 1n Mojo", -175 + 50 * f.loop[cp], -75);
            f.DotShape(cp, 1, "40 + 1n Mojo", -175 + 50 * f.loop[cp], -125);
            f.DotShape(cp, 1, "40 + 1n Mojo", -175 + 50 * f.loop[cp], -175);
            f.DotShape(cp, 1, "Kakaru (Twilight)", 175 - 50 * f.loop[cp], 25);
            f.DotShape(cp, 1, "Kakaru (Twilight)", 175 - 50 * f.loop[cp], 75);
            f.DotShape(cp, 1, "Kakaru (Twilight)", 175 - 50 * f.loop[cp], 125);
            f.DotShape(cp, 1, "Kakaru (Twilight)", 175 - 50 * f.loop[cp], 175);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -175 + 50 * f.loop[cp], -25);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -175 + 50 * f.loop[cp], -75);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -175 + 50 * f.loop[cp], -125);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -175 + 50 * f.loop[cp], -175);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         SetSwitch("Recall - Mayuri", Clear);
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
         f.SkillEnd(cp);
      }
   }
}