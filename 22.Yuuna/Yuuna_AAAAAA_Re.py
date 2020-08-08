import Function as f;

const s = StringBuffer();
function FlowerShape(cp : TrgPlayer, count, Unit : TrgUnit, i, distance, interval);

function main(cp)
{
   MoveLocation("22.Yuuna_Bozo", f.heroID[cp], cp, "Anywhere");
   f.BanReturn(cp);
   f.HoldPosition(cp);
   
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {         
            SetSwitch("Recall - Yuuna", Set);

            f.SkillWait(cp, 2000);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.SkillWait(cp, 3200);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.Voice_Routine(cp, 13);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 4)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 2 * f.loop[cp] + 5, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 2 * f.loop[cp] + 5, 75);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 11, 75);
            f.NxNSquareShape(cp, 1, "60 + 1n Siege", 11, 75);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.SkillWait(cp, 1120);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] == 0)
         {         
            f.SkillWait(cp, 1280);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 4)
      {  
         if (f.loop[cp] < 4)
         {         
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 2 * f.loop[cp] + 5, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 2 * f.loop[cp] + 5, 75);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.SkillWait(cp, 4000);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 5)
      {
         SetSwitch("Recall - Yuuna", Clear);
         SetSwitch("UiltimateSwitch", Clear);
         f.SkillEnd(cp);
      }
   }

   if (f.delayB[cp] == 0)
   {
      if (f.count[cp] == 1)
      {
         if (f.loopB[cp] < 32)
         {
            f.Table_Sin(cp, 50 * f.loopB[cp], 50 + 10 * f.loopB[cp]);
            f.Table_Cos(cp, 50 * f.loopB[cp], 50 + 10 * f.loopB[cp]);

            f.SquareShape(cp, 16, "Rhynadon (Badlands)", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] += 1;
         }
      }
      if (f.count[cp] == 3)
      {
         if (f.loopB[cp] == 0)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 3, 75);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] = 0;
         }
      }
   }
}
