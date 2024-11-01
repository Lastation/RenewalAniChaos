import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {         
            f.SquareShape(cp, 1, "Target", 50, 0);
            f.SquareShape(cp, 1, "Target", 100, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.SquareShape(cp, 1, "Target", 50, 100);
            f.SquareShape(cp, 1, "Target", 100, 50);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Goliath", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 100, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 150);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 100);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 150);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 320);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.DotShape(cp, 1, "40 + 1n Zealot", 50, 0);
            f.DotShape(cp, 1, "40 + 1n Zealot", -50, 0);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Wraith", 50, 0);
            f.DotShape(cp, 1, "40 + 1n Wraith", -50, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Zealot", 0, 50);
            f.DotShape(cp, 1, "40 + 1n Zealot", 0, -50);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Wraith", 0, 50);
            f.DotShape(cp, 1, "40 + 1n Wraith", 0, -50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Zealot", 50, 50);
            f.DotShape(cp, 1, "40 + 1n Zealot", -50, -50);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Wraith", 50, 50);
            f.DotShape(cp, 1, "40 + 1n Wraith", -50, -50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Zealot", -50, 50);
            f.DotShape(cp, 1, "40 + 1n Zealot", 50, -50);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Wraith", -50, 50);
            f.DotShape(cp, 1, "40 + 1n Wraith", 50, -50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         f.SkillEnd(cp);
      }
   }
}