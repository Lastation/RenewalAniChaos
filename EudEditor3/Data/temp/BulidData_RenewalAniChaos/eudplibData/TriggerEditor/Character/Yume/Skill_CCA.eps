import Function as f;

function main(cp)
{
   MoveLocation("26.Yume_Bozo", f.heroID[cp], cp, "Anywhere");
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {             
            SetSwitch("Recall - Yume", Set);
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            f.SkillWait(cp, 400);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 21)
         {
            var deg = (dwrand() % 16) * 22;
            var distance = (dwrand() % 3 + 7) * 10;

            if (f.loop[cp] % 2 == 0)
            {
               RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

               f.LineShape(cp, 1, "40 + 1n Wraith", deg, 9, 75, distance);
               f.LineShape(cp, 1, "60 + 1n High Templar", deg, 9, 75, distance);
            }

            else if (f.loop[cp] % 2 == 1)
            {
               RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

               f.LineShape(cp, 1, " Creep. Dunkelheit", deg, 9, 75, distance);
               f.LineShape(cp, 1, "Target", deg, 9, 75, distance);
            }

            deg = (dwrand() % 16) * 22;
            distance = (dwrand() % 3 + 7) * 10;

            if (f.loop[cp] % 2 == 0)
               f.LineShape(cp, 1, "Kakaru (Twilight)", deg, 9, 75, distance);
            else if (f.loop[cp] % 2 == 1)
               f.LineShape(cp, 1, " Unit. Hoffnung 25000", deg, 9, 75, distance);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
            KillUnitAt(All, "Target", "Anywhere", cp);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 21)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            RemoveUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         SetSwitch("Recall - Yume", Clear);
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

         f.SkillEnd(cp);
      }
   }
}